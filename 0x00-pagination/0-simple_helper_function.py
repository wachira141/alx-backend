#!/usr/bin/env python3
'''
simple helper func
'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    '''
    return a tuple of size tow with start index and an end index
    '''
    page_position = page - 1
    return (page_position * page_size, page * page_size)
