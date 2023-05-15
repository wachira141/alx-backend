#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    '''
    return a tuple of size tow with start index and an end index
    '''
    page_position = page - 1
    return (page_position * page_size, page * page_size)


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
        '''
        Retriev a page with data
        '''

        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        data = self.dataset()
        result = index_range(page, page_size)

        if result[0] > len(data):
            return []
        return data[result[0]: result[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        get hyper method
        '''
        data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)

        total_pages = math.ceil(len(self.__dataset) / page_size)
        details = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if end < len(self.__dataset) else None,
            'prev_page': page - 1 if start > 0 else None,
            'total_pages': total_pages,
        }
        return details
