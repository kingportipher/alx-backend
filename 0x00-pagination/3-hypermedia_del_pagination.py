#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Retrieves a page of data using a resilient index system."""
        data = self.indexed_dataset()

        assert index is not None and 0 <= index < len(data), "Index out of range."

        page_data = []
        next_index = index

        for i in range(page_size):
            if next_index in data:
                page_data.append(data[next_index])
                next_index += 1
            else:
                next_index += 1
                if next_index >= len(data):
                    break

        next_index = next_index if next_index < len(data) else None

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(page_data),
            'data': page_data,
        }

