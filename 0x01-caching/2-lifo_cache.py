#!/usr/bin/python3
""" FIFOCache module"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache

    Args:
        BaseCaching (_type_): _description_
    """

    def __init__(self):
        """__init__
        """
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data
          the item value for the key key
        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = list(self.cache_data.keys())[-1]
            print('DISCARD: ' + str(first_key))
            self.cache_data.pop(first_key)
        self.cache_data[key] = item

    def get(self, key):
        """ return the value in self.cache_data linked to key

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        if key is None:
            return None
        return self.cache_data.get(key)
