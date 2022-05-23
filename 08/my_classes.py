import string
import random


class LRUCache1:
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


class LCSP:
    def __init__(self, str1: str, str2: str):
        self.str1 = str1
        self.str2 = str2
        self.len = self.lcsl()

    def lcsl(self):
        matrix = [
            [0 for i in range(len(self.str2) + 1)]
            for j in range(len(self.str1) + 1)
        ]
        for i in range(1, len(self.str1) + 1):
            for j in range(1, len(self.str2) + 1):
                matrix[i][j] = max(
                    matrix[i - 1][j - 1] +
                    (self.str1[i - 1] == self.str2[j - 1]),
                    matrix[i][j - 1],
                    matrix[i - 1][j],
                )
        return matrix[len(self.str1)][len(self.str2)]


class LCSPslots:
    __slots__ = ("str1", "str2", "len")

    def __init__(self, str1: str, str2: str):
        self.str1 = str1
        self.str2 = str2
        self.len = self.lcsl()

    def lcsl(self):
        matrix = [
            [0 for i in range(len(self.str2) + 1)]
            for j in range(len(self.str1) + 1)
        ]
        for i in range(1, len(self.str1) + 1):
            for j in range(1, len(self.str2) + 1):
                matrix[i][j] = max(
                    matrix[i - 1][j - 1] +
                    (self.str1[i - 1] == self.str2[j - 1]),
                    matrix[i][j - 1],
                    matrix[i - 1][j],
                )
        return matrix[len(self.str1)][len(self.str2)]


def str_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))
