"""Utilities for cleaning and exporting origin rules data.

Candidates must implement :func:`normalize_origin_rules` according to the
instructions in the README.
"""


def normalize_origin_rules(input_excel_path: str, output_csv_path: str) -> None:
    """Normalize an origin rules spreadsheet and write it as CSV.

    The function should:

    1. Combine HS code columns into a six-digit code and drop invalid rows.
    2. Clean the goods description while preserving hierarchy dashes.
    3. Normalize decimal numbers in the rule of origin column using ``.`` as the
       decimal separator.
    4. Add ``Chapter`` and ``Heading`` columns based on the original data.
    5. Write the result to ``output_csv_path`` with column order:
       ``Chapter``, ``Heading``, ``HS Code 6 digits``, ``Goods Description``,
       ``Rule of Origin``.

    Args:
        input_excel_path: Path to the input Excel file.
        output_csv_path: Path to the CSV file that will be created.
    """
    raise NotImplementedError
