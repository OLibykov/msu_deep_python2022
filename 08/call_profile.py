import cProfile
import pstats
import io
import sys
import weakref
from my_classes import LRUCache1, LCSP, LCSPslots, str_generator

if __name__ == "__main__":
    cache = LRUCache1(1_000_000)

    pr = cProfile.Profile()
    pr.enable()

    obj = LCSP("aabcfd", "adabcabc")
    obj_slots = LCSPslots("aabcfd", "adabcabc")
    cache["0"] = obj
    cache["0S"] = obj_slots
    cache["0W"] = weakref.ref(obj)

    print("LCS length: %d %d %d" % (cache["0"].len,
          cache["0S"].len, cache["0W"]().len))
    print(
        "Refcount: %d %d %d"
        % (
            sys.getrefcount(cache["0"]),
            sys.getrefcount(cache["0S"]),
            sys.getrefcount(cache["0W"]()),
        )
    )
    print(
        "Weakrefcount: %d %d %d"
        % (
            weakref.getweakrefcount(cache["0"]),
            weakref.getweakrefcount(cache["0S"]),
            weakref.getweakrefcount(cache["0W"]()),
        )
    )

    # Load:
    for i in range(1, 10001):
        cache[str(i)] = LCSP(str_generator(), str_generator())

    pr.disable()

    out = io.StringIO()
    ps = pstats.Stats(pr, stream=out)
    ps.print_stats()

    print(out.getvalue())
