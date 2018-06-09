import unittest


def solution(A):
    n = len(A)
    s_max_end = [0] * n
    e_max_end = [0] * n
    for i in range(1, n - 1):
        s_max_end[i] = max(0, s_max_end[i - 1] + A[i])
    for i in range(n - 2, 0, -1):
        e_max_end[i] = max(0, e_max_end[i + 1] + A[i])
    max_double = 0
    for i in range(1, n - 1):
        max_double = max(max_double, s_max_end[i - 1] + e_max_end[i + 1])
    return max_double


class MaxDoubleSliceSumTests(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(17, solution([3, 2, 6, -1, 4, 5, -1, 2]))

    def test_example2(self):
        self.assertEqual(17, solution([3, -1, 2, 6, -1, 4, 5, -1, 2]))

    def test_example3(self):
        self.assertEqual(17, solution([3, -1, 2, -1, 6, 4, 5, -1, 2]))

    def test_example4(self):
        self.assertEqual(7, solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))

    def test_example5(self):
        self.assertEqual(17, solution([3, -1, 2, -1, 6, 4, 5, -1, -1, 2]))
