#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
            method with two integer arguments: index with a
            None default value and page_size with default value of 10.
        """
        data = []
        i_data = self.indexed_dataset()
        l_keys = list(i_data.keys())
        assert index + page_size < len(l_keys) and index < len(l_keys)

        if index not in i_data:
            initial_index = l_keys[index]
        else:
            initial_index = index

        for i in range(initial_index, initial_index + page_size):
            if i not in i_data:
                data.append(i_data[l_keys[i]])
            else:
                data.append(i_data[i])

        next_index: int = index + page_size

        if index in l_keys:
            next_index
        else:
            next_index = l_keys[next_index]
        return {
                "index": index,
                "next_index": next_index,
                "page_size": len(data),
                "data": data,
                }
