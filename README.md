# BỘ ĐỀ PHỎNG VẤN PYTHON + XỬ LÝ EXCEL

## 📌 Giới thiệu
Bộ đề này gồm **2 câu hỏi** nhằm kiểm tra kỹ năng lập trình Python, xử lý dữ liệu, và làm việc với file Excel.  
Ứng viên cần:
- Hiểu và xử lý định dạng số khác nhau (hệ dấu chấm / dấu phẩy).
- Làm sạch và chuẩn hoá dữ liệu từ file Excel theo yêu cầu cụ thể.

---

## 📝 Yêu cầu bài làm

### **Câu 1 – Chuẩn hoá số liệu hệ dấu chấm / dấu phẩy**
**Mô tả:**  
Cho một danh sách chuỗi số, mỗi số có thể:
- **Hệ Anh/Mỹ**: Dấu chấm `.` làm số thập phân, dấu phẩy `,` làm phân cách hàng nghìn.
- **Hệ Châu Âu/VN**: Dấu phẩy `,` làm số thập phân, dấu chấm `.` làm phân cách hàng nghìn.

**Nhiệm vụ:**
- Viết hàm Python `normalize_numbers(numbers)` nhận vào **danh sách chuỗi số** và trả về danh sách **float** chuẩn hoá theo hệ Anh/Mỹ (dấu `.` làm số thập phân).
- Có thể đọc dữ liệu từ file `data/numbers_input.txt`.

**Ví dụ Input:**
```

1,234.56
1.234,56
1000
2,5
2.5

```

**Kết quả mong muốn:**
```python
[1234.56, 1234.56, 1000.0, 2.5, 2.5]
```

---

### **Câu 2 – Chuẩn hoá dữ liệu quy tắc xuất xứ (Excel)**

**Mô tả:**
Cho file Excel `data/qtxx_input.xlsx` chứa:

* Mã HS bị chia thành nhiều cột, có dấu chấm/khoảng trắng.
* Mô tả hàng hoá chứa ký tự thừa (`-`, xuống dòng).
* Quy tắc xuất xứ có thể chứa số thập phân với dấu phẩy hoặc dấu chấm.

**Nhiệm vụ:**

1. Gộp các cột mã HS, chuẩn hoá thành đúng 6 chữ số, bỏ dòng không hợp lệ.
2. Chuẩn hoá mô tả hàng hoá:

   * Giữ nguyên dấu `-` để thể hiện phân cấp nhưng loại bỏ khoảng trắng thừa, ký tự xuống dòng.
3. Chuẩn hoá cột Quy tắc xuất xứ về dấu chấm `.` làm số thập phân.
4. Bổ sung các cột “Chương” và “Nhóm” từ dữ liệu gốc.
5. Xuất file CSV với thứ tự cột:

   ```
   Chương, Nhóm, Mã HS 6 số, Mô tả hàng hoá, Quy tắc xuất xứ
   ```
6. Kết quả mong muốn giống file `data/qtxx_expected_output.csv`.

---

## 📂 Cấu trúc thư mục

```
interview_test/
│
├── README.md
├── data/
│   ├── numbers_input.txt
│   ├── qtxx_input.xlsx
│   └── qtxx_expected_output.csv
│
├── src/
│   ├── normalize_numbers.py
│   └── normalize_origin_rules.py
│
├── tests/
│   ├── test_numbers.py
│   └── test_qtxx.py
│
└── requirements.txt
```

---

## ▶️ Cách chạy

1. **Cài thư viện**

```bash
pip install -r requirements.txt
```

2. **Chạy từng bài**

```bash
python src/normalize_numbers.py
python src/normalize_origin_rules.py
```

3. **Chạy toàn bộ test**

```bash
pytest
```

---

## ✅ Yêu cầu nộp bài

* Nộp toàn bộ thư mục `src/` và `tests/`.
* Code phải chạy không lỗi với Python 3.9+.
* Không dùng thư viện ngoài trừ `pandas`, `openpyxl`, `pytest`.

