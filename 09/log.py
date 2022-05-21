import logging
import sys


class LRUCache:
    def __init__(self, limit=42, logger=logging.getLogger()):
        self.log = logger

        if limit <= 0:
            self.log.error("Limit less than 0?!")
            raise RuntimeError("limit must be greater than 0")
        self.limit = limit
        self.queue = []
        self.mylru = {}
        self.log.info("Created instance of LRUCache")

    def get(self, key):
        if key in self.queue:
            self.queue.remove(key)
            self.queue.append(key)
            return self.mylru[key]
        self.log.info(f"Key {key} not found")
        return None

    def set(self, key, value):
        if key in self.queue:
            self.queue.remove(key)
            self.queue.append(key)
            self.mylru[key] = value
            self.log.info(f"Update: {key} -> {value}")
        else:
            if len(self.queue) < self.limit:
                self.queue.append(key)
                self.mylru[key] = value
                self.log.info(f"Set: {key} -> {value}")
            else:
                self.log.warning(
                    f'Queue is full, element with key "{self.queue[0]}" ' +
                    'will be deleted'
                )
                self.mylru.pop(self.queue[0])
                del self.queue[0]
                self.queue.append(key)
                self.mylru[key] = value
                self.log.info(f"Set: {key} -> {value}")
        return self.mylru[key]

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, item, val):
        return self.set(item, val)


if __name__ == "__main__":
    log = logging.getLogger("MyBestLogger")
    log.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s\t%(name)s\t" +
                                  "%(levelname)s\t%(message)s")
    flh = logging.FileHandler("cache.log")
    flh.setLevel(logging.INFO)
    flh.setFormatter(formatter)
    log.addHandler(flh)

    if "-s" in sys.argv:
        formatter = logging.Formatter("%(levelname)s - %(message)s")
        std = logging.StreamHandler(sys.stdout)
        std.setLevel(logging.WARNING)
        std.setFormatter(formatter)
        log.addHandler(std)

    try:
        LRUCache(0, log)
    except RuntimeError:
        pass

    cache = LRUCache(3, log)
    cache["a"] = 1
    cache["b"] = 2
    cache["c"] = 3
    cache["c"] = 3
    cache["a"]
    cache["d"] = 4
