#!/usr/bin/env python3
'''
LIFOCache class to implement a Fifo like caching
system
'''
from base_model import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    '''LIFOCache class
    '''
    def __init__(self):
        '''init the FIFOCache class
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Add an item to the cache
        '''
        if key is None or item is None:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            item_key, _ = self.cache_data.popitem(True)
            print("DISCARD", item_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieve an item using a key
        """
        return self.cache_data.get(key, None)
