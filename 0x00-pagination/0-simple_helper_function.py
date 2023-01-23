#!/usr/bin/env python3
"""
0-simple_helper_function
"""


def index_range(page, page_size):
    """
    Function named index_range:
        that takes two integer arguments page and page_size
    Returns: a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in list for those
    particular pagination parameters.
    """
    prev_page = (page - 1) * page_size
    curr_page = prev_page + page_size
    return (prev_page, curr_page)
