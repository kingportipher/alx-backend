#!/usr/bin/env python3
"""Task 2: Hypermedia pagination
"""

import csv
import math
from typing import Dict, List, Tuple


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
        """Retrieves a page of data from the dataset."""
        assert isinstance(page, int) and isinstance(page_size, int), "Arguments must be integers."
        assert page > 0 and page_size > 0, "Arguments must be greater than 0."

        start, end = index_range(page, page_size)
        data = self.dataset()

        if start >= len(data):
            return []

        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Retrieves information about a page, including hypermedia pagination."""
        data = self.get_page(page, page_size)
        dataset_len = len(self.dataset())
        total_pages = math.ceil(dataset_len / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if (page * page_size) < dataset_len else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }

