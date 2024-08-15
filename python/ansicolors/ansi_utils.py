"""This file contains utilities for convenient module usage leveraging base formatting functions."""

from typing import List, Callable
from functools import reduce


def ANSI_formatter(*formatters: List[Callable[[str], str]]) -> Callable[[str], str]:
    """Composed and return ANSI formatter which applies all the formatters from the
    'formatters' list from the left to the right.
    """

    esc_sequence = reduce(lambda acc, func: func(acc), formatters, "{}")

    def apply(text: str) -> str:
        return esc_sequence.format(text)

    return apply
