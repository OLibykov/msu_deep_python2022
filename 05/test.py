import unittest
from lrucache import LRUCache


class TestLRUCache(unittest.TestCase):

    def test_default(self):
        cache = LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.get("k3"), None)
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")

        cache.set("k3", "val3")

        self.assertEqual(cache.get("k3"), "val3")
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.get("k1"), "val1")

        cache["k1"] = "val1"
        self.assertEqual(cache.get("k3"), "val3")

    def test_my_stupid_test(self):
        # 1
        with self.assertRaises(RuntimeError):
            LRUCache(0)
        # 2
        cache = LRUCache(3)
        cache["a"] = 1
        cache["b"] = 2
        cache["c"] = 3
        self.assertEqual(cache["a"], 1)
        cache["d"] = 4
        self.assertEqual(cache["a"], 1)
        self.assertEqual(cache["b"], None)
        self.assertEqual(cache["c"], 3)
        self.assertEqual(cache["d"], 4)


if __name__ == "__main__":
    unittest.main()
