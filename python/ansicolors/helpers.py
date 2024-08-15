"""Helper functions used across ansicolor module 
which are not exposed to the module user"""


def __rgb6_in_range(value: int) -> bool:
    return value <= 5 and value >= 0


def __rgb_in_range(value: int) -> bool:
    return value <= 255 and value >= 0


def __rgb_to_ansi_code(r: int, g: int, b: int) -> int:
    """Return ANSI code for color specified via provided RGB."""
    return 36 * r + 6 * g + b + 16


def __gray_scale_in_range(value: int) -> bool:
    return 0 <= value and value <= 23
