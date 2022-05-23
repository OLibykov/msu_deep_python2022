import unittest
from customlist import CustomList


class TestCustomList(unittest.TestCase):
    def test_equal_length_customlists(self):

        cl1 = CustomList([1, 2, 3])
        cl2 = CustomList([-1, -2, -3])

        self.assertTrue(cl1 + cl2 == [0, 0, 0])
        self.assertTrue(cl1 - cl2 == [2, 4, 6])
        self.assertTrue(cl2 + cl1 == [0, 0, 0])
        self.assertTrue(cl2 - cl1 == [-2, -4, -6])

    def test_non_equal_length_customlists(self):

        cl1 = CustomList([1, 2, 3])
        cl2 = CustomList([1, 2])

        self.assertTrue(cl1 + cl2 == [2, 4, 3])
        self.assertTrue(cl1 - cl2 == [0, 0, 3])
        self.assertTrue(cl2 + cl1 == [2, 4, 3])
        self.assertTrue(cl2 - cl1 == [0, 0, -3])

    def test_equal_length_customlist_and_list(self):

        cl1 = CustomList([1, 2, 3])
        list1 = [1, 2, 3]

        self.assertTrue(cl1 + list1 == [2, 4, 6])
        self.assertTrue(list1 + cl1 == [2, 4, 6])
        self.assertTrue(cl1 - list1 == [0, 0, 0])
        self.assertTrue(list1 - cl1 == [0, 0, 0])

    def test_non_equal_length_customlist_and_list(self):

        cl1 = CustomList([1, 2, 3])
        list1 = [1, 2]

        self.assertTrue(cl1 + list1 == [2, 4, 3])
        self.assertTrue(cl1 - list1 == [0, 0, 3])
        self.assertTrue(list1 + cl1 == [2, 4, 3])
        self.assertTrue(list1 - cl1 == [0, 0, -3])

        cl2 = CustomList([1, 2])
        list2 = [1, 2, 3]

        self.assertTrue(cl2 + list2 == [2, 4, 3])
        self.assertTrue(list2 + cl2 == [2, 4, 3])
        self.assertTrue(cl2 - list2 == [0, 0, -3])
        self.assertTrue(list2 - cl2 == [0, 0, 3])

    def test_edge_cases(self):

        cl1 = CustomList([])
        list1 = [1, 2]

        self.assertTrue(cl1 + list1 == [1, 2])
        self.assertTrue(cl1 - list1 == [-1, -2])
        self.assertTrue(list1 + cl1 == [1, 2])
        self.assertTrue(list1 - cl1 == [1, 2])

        cl2 = CustomList([1, 2])
        list2 = []

        self.assertTrue(cl2 + list2 == [1, 2])
        self.assertTrue(cl2 - list2 == [1, 2])
        self.assertTrue(list2 + cl2 == [1, 2])
        self.assertTrue(list2 - cl2 == [-1, -2])


if __name__ == "__main__":
    unittest.main()
