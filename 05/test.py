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

    def test_len_1(self):
        cache = LRUCache(1)
        cache["a"] = 1
        self.assertEqual(cache["a"], 1)
        cache["b"] = 2
        self.assertEqual(cache["a"], None)
        self.assertEqual(cache["b"], 2)
        cache["c"] = 3
        cache["d"] = 4
        self.assertEqual(cache["a"], None)
        self.assertEqual(cache["b"], None)
        self.assertEqual(cache["c"], None)
        self.assertEqual(cache["d"], 4)

    def test_complete_displacement(self):
        cache = LRUCache(3)
        cache["a"] = 1
        cache["b"] = 2
        cache["c"] = 3
        self.assertEqual(cache["a"], 1)
        self.assertEqual(cache["b"], 2)
        self.assertEqual(cache["c"], 3)
        cache["d"] = 1
        cache["e"] = 2
        cache["f"] = 3
        self.assertEqual(cache["a"], None)
        self.assertEqual(cache["b"], None)
        self.assertEqual(cache["c"], None)
        self.assertEqual(cache["d"], 1)
        self.assertEqual(cache["e"], 2)
        self.assertEqual(cache["f"], 3)

    def test_replacing_the_value(self):
        cache = LRUCache(3)
        cache["a"] = 1
        cache["b"] = 2
        cache["c"] = 3
        self.assertEqual(cache["a"], 1)
        self.assertEqual(cache["b"], 2)
        self.assertEqual(cache["c"], 3)
        cache["b"] = 4
        self.assertEqual(cache["b"], 4)
        cache["d"] = 1
        self.assertEqual(cache["c"], 3)
        self.assertEqual(cache["b"], 4)
        self.assertEqual(cache["d"], 1)
        cache["e"] = 2
        self.assertEqual(cache["b"], 4)
        self.assertEqual(cache["d"], 1)
        self.assertEqual(cache["e"], 2)
        cache["f"] = 3
        self.assertEqual(cache["b"], None)

    def test_replacing_the_value_without_get(self):
        cache = LRUCache(3)
        cache["a"] = 1
        cache["b"] = 2
        cache["c"] = 3
        cache["b"] = 4
        self.assertTrue("a" in cache.queue)
        self.assertTrue("b" in cache.queue)
        self.assertTrue("c" in cache.queue)
        cache["d"] = 1
        self.assertFalse("a" in cache.queue)
        self.assertTrue("b" in cache.queue)
        self.assertTrue("c" in cache.queue)
        cache["e"] = 2
        self.assertFalse("a" in cache.queue)
        self.assertTrue("b" in cache.queue)
        self.assertFalse("c" in cache.queue)
        cache["f"] = 3
        self.assertFalse("a" in cache.queue)
        self.assertFalse("b" in cache.queue)
        self.assertFalse("c" in cache.queue)
        self.assertTrue("d" in cache.queue)
        self.assertTrue("e" in cache.queue)
        self.assertTrue("f" in cache.queue)


if __name__ == "__main__":
    unittest.main()
