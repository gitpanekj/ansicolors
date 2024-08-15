"""This file contains functions for formatting text with colors from RGB color model."""

from typing import Tuple

# inter module imports
from .helpers import __rgb_in_range


def fg_rgb(rgb: Tuple[int], text: str) -> str:
    """RGB color model foreground"""

    if len(rgb) > 3:
        raise ValueError("Invalid format of rgb.")

    if not all(map(__rgb_in_range, rgb)):
        raise ValueError("Elements of (R,G,B) must range from 0 to 255.")

    (r, g, b) = rgb

    return f"\033[38;2;{r};{g};{b}m{text}\033[m"


def bg_rgb(rgb: Tuple[int], text: str) -> str:
    """RGB color model background"""

    if len(rgb) > 3:
        raise ValueError("Invalid format of rgb.")

    if not all(map(__rgb_in_range, rgb)):
        raise ValueError("Elements of (R,G,B) must range from 0 to 255.")

    (r, g, b) = rgb

    return f"\033[48;2;{r};{g};{b}m{text}\033[m"
