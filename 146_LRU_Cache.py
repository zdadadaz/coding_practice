# double linked list to re-arrange the frequency of occurrence.

from collections import deque


class LRUCache:
    def __init__(self, cache_size):
        self.cache_size = cache_size
        self.queue = deque()
        self.hash_map = dict()

    def is_queue_full(self):
        return len(self.queue) == self.cache_size

    def set(self, key, value):
        if key not in self.hash_map:
            if self.is_queue_full():
                pop_key = self.queue.pop()
                self.hash_map.pop(pop_key)
                self.queue.appendleft(key)
                self.hash_map[key] = value
            else:
                self.queue.appendleft(key)
                self.hash_map[key] = value

    def get(self, key):
        if key not in self.hash_map:
            return -1
        else:
            self.queue.remove(key)
            self.queue.appendleft(key)
            return self.hash_map[key]


if __name__ == '__main__':
    # 設定 cache 大小為 3
    lru_cache = LRUCache(3)

    lru_cache.set('key1', 7)
    lru_cache.set('key2', 2)
    lru_cache.set('key3', 3)
    lru_cache.set('key4', 4)
    print(lru_cache.get('key2'))
    # 超過 cache 大小，被丟棄，所以 key1 回傳值為 -1
    print(lru_cache.get('key1'))
    lru_cache.set('key1', 7)
    # key1 已存在 cache 中，所以不做任何動作
    lru_cache.set('key1', 2)
    print(lru_cache.get('key1'))
