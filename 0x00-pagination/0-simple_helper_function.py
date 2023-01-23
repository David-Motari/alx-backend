#!/usr/bin/env python3
"""
0-simple_helper_function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function named index_range:
        that takes two integer arguments page and page_size
    Returns: a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in list for those
    particular pagination parameters.
    """
    prev_page: int = (page - 1) * page_size
    curr_page: int = prev_page + page_size
    return (prev_page, curr_page)

