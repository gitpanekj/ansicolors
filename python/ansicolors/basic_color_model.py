"""This file contains functions for formatting text with colors from basic color model."""

from .enums import BasicColor


###### Foreground formatters ######
def fg_black(text: str) -> str:
    return f"\033[3{BasicColor.black.value}m{text}\033[m"


def fg_red(text: str) -> str:
    return f"\033[3{BasicColor.red.value}m{text}\033[m"


def fg_green(text: str) -> str:
    return f"\033[3{BasicColor.green.value}m{text}\033[m"


def fg_yellow(text: str) -> str:
    return f"\033[3{BasicColor.yellow.value}m{text}\033[m"


def fg_blue(text: str) -> str:
    return f"\033[3{BasicColor.blue.value}m{text}\033[m"


def fg_magenta(text: str) -> str:
    return f"\033[3{BasicColor.magenta.value}m{text}\033[m"


def fg_cyan(text: str) -> str:
    return f"\033[3{BasicColor.cyan.value}m{text}\033[m"


def fg_white(text: str) -> str:
    return f"\033[3{BasicColor.white.value}m{text}\033[m"


###### Background formatters ######
def bg_black(text: str) -> str:
    return f"\033[4{BasicColor.black.value}m{text}\033[m"


def bg_red(text: str) -> str:
    return f"\033[4{BasicColor.red.value}m{text}\033[m"


def bg_green(text: str) -> str:
    return f"\033[4{BasicColor.green.value}m{text}\033[m"


def bg_yellow(text: str) -> str:
    return f"\033[4{BasicColor.yellow.value}m{text}\033[m"


def bg_blue(text: str) -> str:
    return f"\033[4{BasicColor.blue.value}m{text}\033[m"


def bg_magenta(text: str) -> str:
    return f"\033[4{BasicColor.magenta.value}m{text}\033[m"


def bg_cyan(text: str) -> str:
    return f"\033[4{BasicColor.cyan.value}m{text}\033[m"


def bg_white(text: str) -> str:
    return f"\033[4{BasicColor.white.value}m{text}\033[m"
