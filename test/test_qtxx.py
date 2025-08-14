import os
import re
import pandas as pd
import numpy as np
import pandas.testing as pdt

# Kỳ vọng ứng viên cài đặt hàm này trong src/normalize_origin_rules.py
# Hàm interface:
#   normalize_origin_rules(input_excel_path: str, output_csv_path: str) -> None
from src.normalize_origin_rules import normalize_origin_rules  # noqa: F401


def _resolve(path_rel: str, fallback_abs: str) -> str:
    """Ưu tiên đường dẫn tương đối trong repo (./data/...). Nếu không có, dùng file thật đã cung cấp ở fallback_abs (trong môi trường test)."""
    return path_rel if os.path.exists(path_rel) else fallback_abs


def _clean_df(df: pd.DataFrame) -> pd.DataFrame:
    """Chuẩn hóa nhẹ để so sánh công bằng:
    - Chỉ giữ đúng 5 cột yêu cầu
    - Strip khoảng trắng 2 đầu
    - Thay \n, \t về 1 space
    - Chuẩn hóa khoảng trắng lặp
    - Điền NaN thành chuỗi rỗng
    - Ép cột 'Mã HS 6 số' về chuỗi số không có dấu cách"""
    required_cols = ["Chương", "Nhóm", "Mã HS 6 số", "Mô tả hàng hoá", "Quy tắc xuất xứ"]
    # Đổi tên cột nếu thừa khoảng trắng
    df = df.copy()
    df.columns = [str(c).strip() for c in df.columns]
    # Chỉ lấy các cột yêu cầu (nếu ứng viên tạo thêm cột phụ)
    df = df[required_cols].copy()

    # Chuẩn hóa chuỗi
    for col in required_cols:
        if col == "Mã HS 6 số":
            # Ép về chuỗi số 6 ký tự (nếu người làm xuất int/float)
            df[col] = df[col].astype(str).str.replace(r"\.0+$", "", regex=True)
            df[col] = df[col].str.replace(r"\D", "", regex=True)
        else:
            df[col] = (
                df[col]
                .astype(str)
                .str.replace(r"[\n\r\t]+", " ", regex=True)
                .str.strip()
                .str.replace(r"\s{2,}", " ", regex=True)
            )

    # Điền NaN còn sót
    df = df.replace({np.nan: ""})

    # Sắp xếp để so sánh ổn định
    df = df.sort_values(required_cols).reset_index(drop=True)
    return df


def test_normalize_origin_rules_end_to_end(tmp_path):
    # Xác định đường dẫn input/output
    input_excel = _resolve("data/QTXX.xlsx", "/mnt/data/QTXX.xlsx")
    expected_csv = _resolve("data/qtxx_expected_output.csv", "/mnt/data/qtxx_co_aanz.csv")
    assert os.path.exists(input_excel), f"Không tìm thấy file input: {input_excel}"
    assert os.path.exists(expected_csv), f"Không tìm thấy file expected: {expected_csv}"

    # Đường dẫn output tạm
    out_csv = tmp_path / "qtxx_output.csv"

    # Gọi hàm của ứng viên
    from src.normalize_origin_rules import normalize_origin_rules
    normalize_origin_rules(str(input_excel), str(out_csv))

    # Đọc dữ liệu
    got = pd.read_csv(out_csv, dtype=str, keep_default_na=False)
    exp = pd.read_csv(expected_csv, dtype=str, keep_default_na=False)

    # Chuẩn hóa và so sánh
    got_clean = _clean_df(got)
    exp_clean = _clean_df(exp)

    # So sánh khung dữ liệu sau chuẩn hóa nhẹ
    try:
        pdt.assert_frame_equal(got_clean, exp_clean, check_dtype=False, check_like=False)
    except AssertionError as e:
        # Gợi ý chênh lệch khi fail
        diff_info = []
        if got_clean.shape != exp_clean.shape:
            diff_info.append(f"Shape khác nhau: got={got_clean.shape}, exp={exp_clean.shape}")
        mismatched_cols = [c for c in exp_clean.columns if not got_clean[c].equals(exp_clean[c])]
        if mismatched_cols:
            diff_info.append("Cột khác biệt: " + ", ".join(mismatched_cols[:10]))
        raise AssertionError(
            "Output không khớp expected sau khi chuẩn hóa.\n"
            + "\n".join(diff_info)
            + "\n\nChi tiết pandas:\n"
            + str(e)
        )
