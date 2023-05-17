#!/usr/bin/env python3
'''
FIFOCache class to implement a Fifo like caching
system
'''
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    '''FIFOCache class
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
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            item_key, _ = self.cache_data.popitem(False)
            print("DISCARD", item_key)

    def get(self, key):
        """Retrieve an item using a key
        """
        return self.cache_data.get(key, None)
