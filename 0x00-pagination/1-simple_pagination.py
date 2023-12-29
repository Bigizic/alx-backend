#!/usr/bin/python3
""" a method named get_page that takes two integer arguments
page with default value 1 and page_size with default value 10.
"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """return a tuple of size two containing a start index and
    an end index corresponding to the range of indexes to return
    in a list for those particular pagination parameters.
    @param (page): <int>
    @param (page_size): <int>
    Return: <tuple>
    """
    return (((page - 1) * (page_size)), (page * page_size))


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
        """like index range
        """
        assert isinstance(page, int) and page > 0, AssertionError
        assert isinstance(page_size, int) and page_size > 0, AssertionError
        temp = index_range(page, page_size)
        result = self.dataset()[temp[0]:temp[1]]
        if result:
            return result
        return []
