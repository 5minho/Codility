import unittest


def solution(A, B):
    n = len(A)
    fibo = [1] * (n + 1)

    for i in range(2, n + 1):
        fibo[i] = (fibo[i - 1] + fibo[i - 2])

    result = [0] * n
    for i in range(n):
        result[i] = fibo[A[i]] & ((1 << B[i]) - 1)

    return result


class LadderTests(unittest.TestCase):

    def test_example1(self):
        self.assertEqual([5, 1, 8, 0, 1], solution([4, 4, 5, 5, 1], [3, 2, 4, 3, 1]))

    def test_example2(self):
        self.assertEqual([1], solution([1], [30]))
