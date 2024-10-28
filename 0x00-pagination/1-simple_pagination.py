#!/usr/bin/env python3
"""
Main file
"""


import csv
from typing import List
import math


def index_range(page: int, page_size: int) -> tuple:
    """_summary_

    Args:
        page (int): _description_
        page_size (int): _description_

    Returns:
        tuple: _description_
    """
    return (page*page_size-page_size, page_size*page)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """_summary_

            Args:
                page (int, optional): _description_. Defaults to 1.
                page_size (int, optional): _description_. Defaults to 10.

            Returns:
                List[List]: _description_
        """
        assert (type(page) == int and page > 0)
        assert (type(page_size) == int and page_size > 0)
        self.dataset()
        set_range = index_range(page, page_size)

        if set_range[0] > len(self.__dataset):
            return []
        return self.__dataset[set_range[0]:set_range[1]]
