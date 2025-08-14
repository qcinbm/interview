"""Normalization helpers for numeric strings.

This module defines :func:`normalize_numbers` that candidates must implement.
"""

from typing import Iterable, List, Optional


def normalize_numbers(numbers: Iterable[str]) -> List[Optional[float]]:
    """Normalize a list of numeric strings to floats.

    The input may contain either English/American format using ``.`` as the decimal
    separator and ``,``, as the thousands separator, or European/Vietnamese format
    using ``,`` as the decimal separator and ``.`` as the thousands separator.

    Args:
        numbers: An iterable of strings representing numbers.

    Returns:
        A list of floats parsed from ``numbers``. If a value cannot be converted,
        ``None`` should be returned at the corresponding position.
    """
    raise NotImplementedError
