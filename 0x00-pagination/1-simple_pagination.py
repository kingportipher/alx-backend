#!/usr/bin/env python3
"""Task 1: Simple pagination.
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range from a given page and page size."""
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a page of data from the dataset.
        
        Args:
            page (int): The page number, starting from 1.
            page_size (int): The number of items per page.
        
        Returns:
            List[List]: A list of rows corresponding to the given page.
        """
        assert type(page) == int and type(page_size) == int, "Arguments must be integers."
        assert page > 0 and page_size > 0, "Arguments must be greater than 0."

        start, end = index_range(page, page_size)
        data = self.dataset()

        if start >= len(data):
            return []

        return data[start:end]

