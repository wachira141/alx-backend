#!/usr/bin/env python3
'''
create a BasicCache class and inherit 
from BaseCaching
'''
from base_model import BaseCaching


class BasicCache(BaseCaching):
    '''
    class to inherit from BaseCaching
    methods:
        def put -  add the supplied key value into the dict
        def get - getter method to get values in the cache_data
    '''
    def put(self, key, item):
        '''add new values to the cache_data dictionary
        '''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''getter method to retrieve value associated
        by with the key
        '''
        return self.cache_data.get(key, None)
