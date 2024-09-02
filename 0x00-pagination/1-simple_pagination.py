import csv
from typing import List

class Server:
    """Server class to paginate a database of popular baby names."""
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
        """Get a page from the dataset based on page number and page size."""
        assert isinstance(page, int) and page > 0, "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        start_idx, end_idx = index_range(page, page_size)
        data = self.dataset()
        
        if start_idx >= len(data):
            return []

        return data[start_idx:end_idx]

def index_range(page: int, page_size: int) -> tuple:
    """Calculate start and end index for a page."""
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
