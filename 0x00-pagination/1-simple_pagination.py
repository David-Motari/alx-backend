#!/usr/bin/env python3
"""
1-simple_pagination
"""
import csv
import math
from typing import List, Tuple


class Server:
    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        rnge: Tuple = index_range(page, page_size)
        self.dataset()
        return self.__dataset[rnge[0]:rnge[1]]


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
