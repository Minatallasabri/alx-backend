#!/usr/bin/python3
""" BasicCache module"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """caching system that inherits from BaseCaching"""

    def __init__(self):
        """_summary_
        """
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value for the key key
        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key is not None and item is not None:
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
