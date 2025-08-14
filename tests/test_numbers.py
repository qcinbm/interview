from src.normalize_numbers import normalize_numbers


def test_normalize_numbers():
    numbers = [
        "1,234.56",  # English/American format
        "1.234,56",  # European/Vietnamese format
        "1000",      # No separator
        "2,5",       # European/Vietnamese format
        "2.5"        # English/American format
    ]
    expected = [1234.56, 1234.56, 1000.0, 2.5, 2.5]
    result = normalize_numbers(numbers)
    assert result == expected
