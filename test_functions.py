import operator
from functools import reduce

from unittest import TestCase, main

from mod2 import _min, _max, _sum, _mult

test_lists = [
    [0],
    [1],
    [1, 2, 3],
    [-55, 7, -30, -2, 23]
]


class FunctionsTest(TestCase):
    def test_min(self):
        for test_list in test_lists:
            self.assertEqual(_min(test_list), min(test_list))

    def test_max(self):
        for test_list in test_lists:
            self.assertEqual(_max(test_list), max(test_list))

    def test_sum(self):
        for test_list in test_lists:
            self.assertEqual(_sum(test_list), sum(test_list))

    def test_mult(self):
        for test_list in test_lists:
            self.assertEqual(_mult(test_list), reduce(operator.mul, test_list))

    def test_empty_list(self):
        self.assertRaises(ValueError, lambda: _max([]))
        self.assertRaises(ValueError, lambda: _min([]))
        self.assertEqual(_sum([]), 0)
        self.assertEqual(_mult([]), 1)


if __name__ == '__main__':
    main()
