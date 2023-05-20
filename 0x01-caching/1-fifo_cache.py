from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Get the first item (oldest) in the cache
            first_item = next(iter(self.cache_data))
            # Remove the first item from the cache
            del self.cache_data[first_item]
            print("DISCARD:", first_item)

        # Assign the item value to the key in the cache
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
