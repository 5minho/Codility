import unittest


def solution(A):
    if len(A) == 0:
        return 0
    max_profit, min_slice = 0, A[0]
    for a in A[1:]:
        max_profit = max(max_profit, a - min_slice)
        min_slice = min(a, min_slice)
    return max_profit


class MaxProfitTests(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(356, solution([23171, 21011, 21123, 21366, 21013, 21367]))

    def test_example2(self):
        self.assertEqual(0, solution([1]))

    def test_example3(self):
        self.assertEqual(0, solution([1, 1, 1, 1, 1, 1]))

    def test_example4(self):
        self.assertEqual(5, solution([1, 2, 3, 4, 5, 6]))

    def test_exapmle5(self):
        self.assertEqual(0, solution([5, 4, 3, 2, 1]))




