import unittest

MIN = -1_000_000


def solution(A):
    max_slice = max_ending = MIN
    for a in A:
        max_ending = max(0, max_ending) + a
        max_slice = max(max_slice, max_ending)
    return max_slice


class MaxSliceSumTests(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(5, solution([3, 2, -6, 4, 0]))

    def test_example2(self):
        self.assertEqual(5, solution([1, 1, 1, 1, 1]))

    def test_example3(self):
        self.assertEqual(-1000000, solution([-1000000]))

    def test_example4(self):
        self.assertEqual(1, solution([-1000000, 1]))

    def test_example5(self):
        self.assertEqual(-999999, solution([-1000000, -999999]))
