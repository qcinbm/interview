import pytest
from src.normalize_numbers import normalize_numbers

def test_normalize_numbers():
    numbers = [
        "1,234.56",  # Anh/Mỹ
        "1.234,56",  # Châu Âu/VN
        "1000",      # Không phân cách
        "2,5",       # Châu Âu/VN
        "2.5"        # Anh/Mỹ
    ]
    expected = [1234.56, 1234.56, 1000.0, 2.5, 2.5]
    result = normalize_numbers(numbers)
    assert result == expected
