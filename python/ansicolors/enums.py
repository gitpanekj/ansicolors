"""This file contains enumerations for basic color codes and font effects codes."""

from enum import IntEnum


# Basic color codes
class BasicColor(IntEnum):
    black = 0
    red = 1
    green = 2
    yellow = 3
    blue = 4
    magenta = 5
    cyan = 6
    white = 7


# Font effect codes
class FontEffect(IntEnum):
    bold = 1
    faint = 2
    italic = 3
    underline = 4
    slow_blink = 5
