"""This file contains functions for formatting text with text effects."""

# inter module imports
from .enums import FontEffect


def bold(text: str) -> str:
    return f"\033[{FontEffect.bold.value}m{text}\033[m"


def faint(text: str) -> str:
    return f"\033[{FontEffect.faint.value}m{text}\033[m"


def italic(text: str) -> str:
    return f"\033[{FontEffect.italic.value}m{text}\033[m"


def underline(text: str) -> str:
    return f"\033[{FontEffect.underline.value}m{text}\033[m"


def slow_blink(text: str) -> str:
    return f"\033[{FontEffect.slow_blink.value}m{text}\033[m"
