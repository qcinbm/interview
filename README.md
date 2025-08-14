# PYTHON + EXCEL INTERVIEW TASKS

## Introduction
This repository contains two exercises designed to evaluate Python programming, data cleaning, and Excel processing skills. Candidates are expected to:

- Handle different numeric formats (comma and period as decimal or thousands separators).
- Clean and standardize data from an Excel file according to specific rules.

---

## Tasks

### 1. Normalize Number Formats
**Description**

Given a list of numeric strings where:
- **English/American format** uses a period `.` for decimals and a comma `,` for thousands.
- **European/Vietnamese format** uses a comma `,` for decimals and a period `.` for thousands.

**Requirement**

Implement `normalize_numbers(numbers)` that accepts a list of strings and returns a list of floats normalized to the English/American format. Input may also be provided in `data/numbers_input.txt`.

**Example**

Input:
```
1,234.56
1.234,56
1000
2,5
2.5
```

Output:
```python
[1234.56, 1234.56, 1000.0, 2.5, 2.5]
```

---

### 2. Normalize Rules of Origin Data (Excel)

**Description**

The Excel file `data/QTXX.xlsx` contains:
- HS codes split across multiple columns with dots or spaces.
- Goods descriptions containing extra characters (`-`, line breaks).
- Rules of origin that may use either commas or periods for decimals.

**Requirement**

1. Combine HS code columns into a six-digit code and drop invalid rows.
2. Clean the goods description while preserving hierarchy dashes and removing extra whitespace or line breaks.
3. Normalize decimal numbers in the rule of origin column using `.` as the decimal separator.
4. Add the columns **Chapter** and **Heading** from the original data.
5. Export a CSV file with the column order:

```
Chapter, Heading, HS Code 6 digits, Goods Description, Rule of Origin
```

6. The result should match `data/qtxx_expected_output.csv`.

---

## Project Structure

```
.
├── README.md
├── requirements.txt
├── data/
│   ├── numbers_input.txt
│   ├── QTXX.xlsx
│   └── qtxx_expected_output.csv
├── src/
│   ├── __init__.py
│   ├── normalize_numbers.py
│   └── normalize_origin_rules.py
└── tests/
    ├── test_numbers.py
    └── test_qtxx.py
```

---

## Usage

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run individual scripts**
   ```bash
   python src/normalize_numbers.py
   python src/normalize_origin_rules.py
   ```

3. **Run all tests**
   ```bash
   pytest
   ```

---

## Submission Requirements

- Submit the complete `src/` and `tests/` directories.
- Code must run without errors on Python 3.9+.
- Only use standard libraries plus `pandas`, `openpyxl`, and `pytest`.
