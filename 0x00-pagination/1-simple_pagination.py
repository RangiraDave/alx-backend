#!/usr/bin/env python3
"""
This module provides a pagination helper function.
"""

import csv
import math
from typing import List
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    Parameters:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and the end index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)


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
        """
        Get the requested page from the dataset
        """
        assert isinstance(page, int) and page > 0, "Page must be a positive\
             integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must\
             be a positive integer"

        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)

        if page > total_pages:
            return []

        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        return dataset[start_index:end_index]
