import unittest
from customlist import CustomList


class TestCustomList(unittest.TestCase):
    def test_equal_length_customlists(self):

        cl1 = CustomList([1, 2, 3])
        cl2 = CustomList([-1, -2, -3])

        test_sum = [0, 0, 0]
        test_cl1_sub_cl2 = [2, 4, 6]
        test_cl2_sub_cl1 = [-2, -4, -6]

        self.assertTrue(
            (cl1 + cl2)[0] == test_sum[0]
            and (cl1 + cl2)[1] == test_sum[1]
            and (cl1 + cl2)[2] == test_sum[2]
        )

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(cl2[0] == -1 and cl2[1] == -2 and cl2[2] == -3)

        self.assertTrue(
            (cl1 - cl2)[0] == test_cl1_sub_cl2[0]
            and (cl1 - cl2)[1] == test_cl1_sub_cl2[1]
            and (cl1 - cl2)[2] == test_cl1_sub_cl2[2]
        )

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(cl2[0] == -1 and cl2[1] == -2 and cl2[2] == -3)

        self.assertTrue(
            (cl2 + cl1)[0] == test_sum[0]
            and (cl2 + cl1)[1] == test_sum[1]
            and (cl2 + cl1)[2] == test_sum[2]
        )

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(cl2[0] == -1 and cl2[1] == -2 and cl2[2] == -3)

        self.assertTrue(
            (cl2 - cl1)[0] == test_cl2_sub_cl1[0]
            and (cl2 - cl1)[1] == test_cl2_sub_cl1[1]
            and (cl2 - cl1)[2] == test_cl2_sub_cl1[2]
        )

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(cl2[0] == -1 and cl2[1] == -2 and cl2[2] == -3)

    def test_non_equal_length_customlists(self):

        cl1 = CustomList([1, 2, 3])
        cl2 = CustomList([1, 2])

        test_sum = [2, 4, 3]
        test_cl1_sub_cl2 = [0, 0, 3]
        test_cl2_sub_cl1 = [0, 0, -3]

        self.assertTrue(
            (cl1 + cl2)[0] == test_sum[0]
            and (cl1 + cl2)[1] == test_sum[1]
            and (cl1 + cl2)[2] == test_sum[2]
        )

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(cl2[0] == 1 and cl2[1] == 2)

        self.assertTrue(
            (cl1 - cl2)[0] == test_cl1_sub_cl2[0]
            and (cl1 - cl2)[1] == test_cl1_sub_cl2[1]
            and (cl1 - cl2)[2] == test_cl1_sub_cl2[2]
        )

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(cl2[0] == 1 and cl2[1] == 2)

        self.assertTrue(
            (cl2 + cl1)[0] == test_sum[0]
            and (cl2 + cl1)[1] == test_sum[1]
            and (cl2 + cl1)[2] == test_sum[2]
        )

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(cl2[0] == 1 and cl2[1] == 2)

        self.assertTrue(
            (cl2 - cl1)[0] == test_cl2_sub_cl1[0]
            and (cl2 - cl1)[1] == test_cl2_sub_cl1[1]
            and (cl2 - cl1)[2] == test_cl2_sub_cl1[2]
        )

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(cl2[0] == 1 and cl2[1] == 2)

    def test_equal_length_customlist_and_list(self):

        cl1 = CustomList([1, 2, 3])
        l_1 = [1, 2, 3]

        test_sum = [2, 4, 6]
        test_cl1_sub_l_1 = [0, 0, 0]
        test_l_1_sub_cl1 = [0, 0, 0]

        self.assertTrue(
            (cl1 + l_1)[0] == test_sum[0]
            and (cl1 + l_1)[1] == test_sum[1]
            and (cl1 + l_1)[2] == test_sum[2]
        )

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(l_1[0] == 1 and l_1[1] == 2 and l_1[2] == 3)

        self.assertTrue(
            (l_1 + cl1)[0] == test_sum[0]
            and (l_1 + cl1)[1] == test_sum[1]
            and (l_1 + cl1)[2] == test_sum[2]
        )

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(l_1[0] == 1 and l_1[1] == 2 and l_1[2] == 3)

        self.assertTrue(
            (cl1 - l_1)[0] == test_cl1_sub_l_1[0]
            and (cl1 - l_1)[1] == test_cl1_sub_l_1[1]
            and (cl1 - l_1)[2] == test_cl1_sub_l_1[2]
        )

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(l_1[0] == 1 and l_1[1] == 2 and l_1[2] == 3)

        self.assertTrue(
            (l_1 - cl1)[0] == test_l_1_sub_cl1[0]
            and (l_1 - cl1)[1] == test_l_1_sub_cl1[1]
            and (l_1 - cl1)[2] == test_l_1_sub_cl1[2]
        )

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(l_1[0] == 1 and l_1[1] == 2 and l_1[2] == 3)

    def test_non_equal_length_customlist_and_list(self):

        cl1 = CustomList([1, 2, 3])
        l_1 = [1, 2]

        test_sum = [2, 4, 3]
        test_cl1_sub_l_1 = [0, 0, 3]
        test_l_1_sub_cl1 = [0, 0, -3]

        self.assertTrue(
            (cl1 + l_1)[0] == test_sum[0]
            and (cl1 + l_1)[1] == test_sum[1]
            and (cl1 + l_1)[2] == test_sum[2]
        )

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(l_1[0] == 1 and l_1[1] == 2)

        self.assertTrue(
            (cl1 - l_1)[0] == test_cl1_sub_l_1[0]
            and (cl1 - l_1)[1] == test_cl1_sub_l_1[1]
            and (cl1 - l_1)[2] == test_cl1_sub_l_1[2]
        )

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(l_1[0] == 1 and l_1[1] == 2)

        self.assertTrue(
            (l_1 + cl1)[0] == test_sum[0]
            and (l_1 + cl1)[1] == test_sum[1]
            and (l_1 + cl1)[2] == test_sum[2]
        )

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(l_1[0] == 1 and l_1[1] == 2)

        self.assertTrue(
            (l_1 - cl1)[0] == test_l_1_sub_cl1[0]
            and (l_1 - cl1)[1] == test_l_1_sub_cl1[1]
            and (l_1 - cl1)[2] == test_l_1_sub_cl1[2]
        )

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(l_1[0] == 1 and l_1[1] == 2)

        cl2 = CustomList([1, 2])
        l_2 = [1, 2, 3]

        test_sum = [2, 4, 3]
        test_cl2_sub_l_2 = [0, 0, -3]
        test_l_2_sub_cl2 = [0, 0, 3]

        self.assertTrue(
            (cl2 + l_2)[0] == test_sum[0]
            and (cl2 + l_2)[1] == test_sum[1]
            and (cl2 + l_2)[2] == test_sum[2]
        )

        self.assertTrue(cl2[0] == 1 and cl1[1] == 2)
        self.assertTrue(l_2[0] == 1 and l_2[1] == 2 and l_2[2] == 3)

        self.assertTrue(
            (l_2 + cl2)[0] == test_sum[0]
            and (l_2 + cl2)[1] == test_sum[1]
            and (l_2 + cl2)[2] == test_sum[2]
        )

        self.assertTrue(cl2[0] == 1 and cl1[1] == 2)
        self.assertTrue(l_2[0] == 1 and l_2[1] == 2 and l_2[2] == 3)

        self.assertTrue(
            (cl2 - l_2)[0] == test_cl2_sub_l_2[0]
            and (cl2 - l_2)[1] == test_cl2_sub_l_2[1]
            and (cl2 - l_2)[2] == test_cl2_sub_l_2[2]
        )

        self.assertTrue(cl2[0] == 1 and cl1[1] == 2)
        self.assertTrue(l_2[0] == 1 and l_2[1] == 2 and l_2[2] == 3)

        self.assertTrue(
            (l_2 - cl2)[0] == test_l_2_sub_cl2[0]
            and (l_2 - cl2)[1] == test_l_2_sub_cl2[1]
            and (l_2 - cl2)[2] == test_l_2_sub_cl2[2]
        )

        self.assertTrue(cl2[0] == 1 and cl1[1] == 2)
        self.assertTrue(l_2[0] == 1 and l_2[1] == 2 and l_2[2] == 3)

    def test_edge_cases(self):

        cl1 = CustomList([])
        l_1 = [1, 2]

        test_sum = [1, 2]
        test_cl1_sub_l_1 = [-1, -2]
        test_l_1_sub_cl1 = [1, 2]

        self.assertTrue((cl1 + l_1)[0] == test_sum[0]
                        and (cl1 + l_1)[1] == test_sum[1])

        self.assertTrue(not cl1)
        self.assertTrue(l_1[0] == 1 and l_1[1] == 2)

        self.assertTrue(
            (cl1 - l_1)[0] == test_cl1_sub_l_1[0]
            and (cl1 - l_1)[1] == test_cl1_sub_l_1[1]
        )

        self.assertTrue(not cl1)
        self.assertTrue(l_1[0] == 1 and l_1[1] == 2)

        self.assertTrue((l_1 + cl1)[0] == test_sum[0]
                        and (l_1 + cl1)[1] == test_sum[1])

        self.assertTrue(not cl1)
        self.assertTrue(l_1[0] == 1 and l_1[1] == 2)

        self.assertTrue(
            (l_1 - cl1)[0] == test_l_1_sub_cl1[0] and
            (l_1 - cl1)[1] == test_l_1_sub_cl1[1]
        )

        self.assertTrue(not cl1)
        self.assertTrue(l_1[0] == 1 and l_1[1] == 2)

        cl2 = CustomList([1, 2])
        l_2 = []

        test_sum = [1, 2]
        test_l_2_sub_cl2 = [-1, -2]
        test_cl2_sub_l_2 = [1, 2]

        self.assertTrue((cl2 + l_2)[0] == test_sum[0]
                        and (cl2 + l_2)[1] == test_sum[1])

        self.assertTrue(cl2[0] == 1 and cl2[1] == 2)
        self.assertTrue(not l_2)

        self.assertTrue(
            (cl2 - l_2)[0] == test_cl2_sub_l_2[0]
            and (cl2 - l_2)[1] == test_cl2_sub_l_2[1]
        )

        self.assertTrue(cl2[0] == 1 and cl2[1] == 2)
        self.assertTrue(not l_2)

        self.assertTrue((l_2 + cl2)[0] == test_sum[0]
                        and (l_2 + cl2)[1] == test_sum[1])

        self.assertTrue(cl2[0] == 1 and cl2[1] == 2)
        self.assertTrue(not l_2)

        self.assertTrue(
            (l_2 - cl2)[0] == test_l_2_sub_cl2[0]
            and (l_2 - cl2)[1] == test_l_2_sub_cl2[1]
        )

        self.assertTrue(cl2[0] == 1 and cl2[1] == 2)
        self.assertTrue(not l_2)

    def test_equivalence(self):

        cl1 = CustomList([1, 2, 3])
        cl2 = CustomList([1, 2, 3])
        cl3 = CustomList([1, 2, 2])
        cl4 = CustomList([1, 5])

        self.assertTrue(cl1 == cl2)

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(cl2[0] == 1 and cl2[1] == 2 and cl2[2] == 3)
        self.assertTrue(cl3[0] == 1 and cl3[1] == 2 and cl3[2] == 2)
        self.assertTrue(cl4[0] == 1 and cl4[1] == 5)

        self.assertFalse(cl1 != cl2)

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(cl2[0] == 1 and cl2[1] == 2 and cl2[2] == 3)
        self.assertTrue(cl3[0] == 1 and cl3[1] == 2 and cl3[2] == 2)
        self.assertTrue(cl4[0] == 1 and cl4[1] == 5)

        self.assertTrue(cl1 <= cl2)

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(cl2[0] == 1 and cl2[1] == 2 and cl2[2] == 3)
        self.assertTrue(cl3[0] == 1 and cl3[1] == 2 and cl3[2] == 2)
        self.assertTrue(cl4[0] == 1 and cl4[1] == 5)

        self.assertTrue(cl1 >= cl2)

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(cl2[0] == 1 and cl2[1] == 2 and cl2[2] == 3)
        self.assertTrue(cl3[0] == 1 and cl3[1] == 2 and cl3[2] == 2)
        self.assertTrue(cl4[0] == 1 and cl4[1] == 5)

        self.assertFalse(cl1 == cl3)

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(cl2[0] == 1 and cl2[1] == 2 and cl2[2] == 3)
        self.assertTrue(cl3[0] == 1 and cl3[1] == 2 and cl3[2] == 2)
        self.assertTrue(cl4[0] == 1 and cl4[1] == 5)

        self.assertFalse(cl3 > cl1)

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(cl2[0] == 1 and cl2[1] == 2 and cl2[2] == 3)
        self.assertTrue(cl3[0] == 1 and cl3[1] == 2 and cl3[2] == 2)
        self.assertTrue(cl4[0] == 1 and cl4[1] == 5)

        self.assertTrue(cl3 < cl4)

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(cl2[0] == 1 and cl2[1] == 2 and cl2[2] == 3)
        self.assertTrue(cl3[0] == 1 and cl3[1] == 2 and cl3[2] == 2)
        self.assertTrue(cl4[0] == 1 and cl4[1] == 5)

        self.assertTrue(cl1 == cl4)

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(cl2[0] == 1 and cl2[1] == 2 and cl2[2] == 3)
        self.assertTrue(cl3[0] == 1 and cl3[1] == 2 and cl3[2] == 2)
        self.assertTrue(cl4[0] == 1 and cl4[1] == 5)

    def test_types(self):

        cl1 = CustomList([1, 2, 3])
        cl2 = CustomList([1, 2])
        l_1 = [1, 2, 3]

        self.assertTrue(isinstance(cl1 + cl2, CustomList))

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(cl2[0] == 1 and cl2[1] == 2)
        self.assertTrue(l_1[0] == 1 and l_1[1] == 2 and l_1[2] == 3)

        self.assertTrue(isinstance(cl1 - cl2, CustomList))

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(cl2[0] == 1 and cl2[1] == 2)
        self.assertTrue(l_1[0] == 1 and l_1[1] == 2 and l_1[2] == 3)

        self.assertTrue(isinstance(cl1 + l_1, CustomList))

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(cl2[0] == 1 and cl2[1] == 2)
        self.assertTrue(l_1[0] == 1 and l_1[1] == 2 and l_1[2] == 3)

        self.assertTrue(isinstance(cl1 - l_1, CustomList))

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(cl2[0] == 1 and cl2[1] == 2)
        self.assertTrue(l_1[0] == 1 and l_1[1] == 2 and l_1[2] == 3)

        self.assertTrue(isinstance(l_1 + cl1, CustomList))

        self.assertTrue(cl1[0] == 1 and cl1[1] == 2 and cl1[2] == 3)
        self.assertTrue(cl2[0] == 1 and cl2[1] == 2)
        self.assertTrue(l_1[0] == 1 and l_1[1] == 2 and l_1[2] == 3)


if __name__ == "__main__":
    unittest.main()
