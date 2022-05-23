import weakref
from memory_profiler import profile
from my_classes import LRUCache1, LCSP, LCSPslots, str_generator


@profile
def load():
    cache = LRUCache1(1_000_000)
    str1, str2 = str_generator(2), str_generator(2)

    for i in range(1, 20001):
        cache[str(i)] = ""
        cache[str(i) + "S"] = ""
        cache[str(i) + "W"] = ""

    for i in range(1, 20001):
        cache[str(i)] = LCSP(str1, str2)

    for i in range(1, 20001):
        cache[str(i) + "W"] = weakref.ref(cache[str(i)])

    for i in range(1, 20001):
        cache[str(i) + "S"] = LCSPslots(str1, str2)

    print("The End Of Time")


if __name__ == "__main__":
    load()
