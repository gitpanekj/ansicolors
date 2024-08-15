"""This file contains functions for formatting text with colors from 8-bit color model."""

from typing import Tuple

# inter module imports
from .enums import BasicColor
from .helpers import __rgb6_in_range, __rgb_to_ansi_code, __gray_scale_in_range


# grayscale ANSI code values range from 232-255 but module defines
# grayscale value in range 0-23 (black to white) for easier use
GRAY_SCALE_OFFSET = 232


def fg_basic_color(color: BasicColor, text: str) -> str:
    """Basic color foreground"""
    return f"\033[38;5;{color.value}m{text}\033[m"


def fg_rgb6(rgb: Tuple[int], text: str) -> str:
    """6x6x6 cube foreground"""
    if len(rgb) > 3:
        raise ValueError("Invalid format of rgb.")
    if not all(map(__rgb6_in_range, rgb)):
        raise ValueError("Elements of (R,G,B) must range from 0 to 5.")

    color_code = __rgb_to_ansi_code(*rgb)

    return f"\033[38;5;{color_code}m{text}\033[m"


def fg_gray_scale(value: int, text: str) -> str:
    """Gray scale foreground"""

    if not __gray_scale_in_range(value):
        raise ValueError("Gray scale value must range from 0 to 23.")

    gs_code = GRAY_SCALE_OFFSET + value

    return f"\033[38;5;{gs_code}m{text}\033[m"


def bg_basic_color(color: BasicColor, text: str) -> str:
    """Basic color background"""

    return f"\033[48;5;{color.value}m{text}\033[m"


def bg_rgb6(rgb: Tuple[int], text: str) -> str:
    """6x6x6 cube background"""

    if len(rgb) > 3:
        raise ValueError("Invalid format of rgb.")
    if not all(map(__rgb6_in_range, rgb)):
        raise ValueError("Elements of (R,G,B) must range from 0 to 5.")

    color_code = __rgb_to_ansi_code(*rgb)

    return f"\033[48;5;{color_code}m{text}\033[m"


def bg_gray_scale(value: int, text: str) -> str:
    """Gray scale background"""

    if not __gray_scale_in_range(value):
        raise ValueError("Gray scale value must range from 0 to 23.")

    gs_code = GRAY_SCALE_OFFSET + value

    return f"\033[48;5;{gs_code}m{text}\033[m"
