class LRUCache:

    def __init__(self, limit=42):
        if limit <= 0:
            raise RuntimeError("limit must be greater than 0")
        self.limit = limit
        self.queue = []
        self.mylru = {}

    def get(self, key):
        if key in self.queue:
            self.queue.remove(key)
            self.queue.append(key)
            return self.mylru[key]
        return None

    def set(self, key, value):
        if key in self.queue:
            self.queue.remove(key)
            self.queue.append(key)
            self.mylru[key] = value
        else:
            if len(self.queue) < self.limit:
                self.queue.append(key)
                self.mylru[key] = value
            else:
                self.mylru.pop(self.queue[0])
                del self.queue[0]
                self.queue.append(key)
                self.mylru[key] = value
        return self.mylru[key]

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, item, val):
        return self.set(item, val)
