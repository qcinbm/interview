import re

def normalize_numbers(numbers):
    result = []
    for num in numbers:
        if num is None:
            result.append(None)
            continue
        
        s = str(num).strip()
        
        # Nếu cả dấu phẩy và dấu chấm đều xuất hiện
        if "," in s and "." in s:
            if s.find(",") < s.find("."):
                # Định dạng Anh/Mỹ: 1,234.56 -> bỏ dấu phẩy
                s = s.replace(",", "")
            else:
                # Định dạng Châu Âu/VN: 1.234,56 -> bỏ dấu chấm, thay dấu phẩy bằng dấu chấm
                s = s.replace(".", "").replace(",", ".")
        elif "," in s:
            # Chỉ có dấu phẩy -> dấu phẩy là dấu thập phân
            s = s.replace(",", ".")
        else:
            # Chỉ có dấu chấm hoặc không có
            pass
        
        try:
            result.append(float(s))
        except ValueError:
            result.append(None)
    return result

if __name__ == "__main__":
    # Đọc file input
    with open("data/numbers_input.txt", "r", encoding="utf-8") as f:
        numbers_list = [line.strip() for line in f if line.strip()]
    print(normalize_numbers(numbers_list))
