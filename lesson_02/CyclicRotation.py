import unittest


def solution(A, K):
    if not A:
        return []
    for i in range(K):
        last = A.pop()
        A.insert(0, last)
    return A


class CyclicRotationTests(unittest.TestCase):

    def test_example1(self):
        self.assertEqual([3, 1, 2], solution([1, 2, 3], 1))

    def test_example2(self):
        self.assertEqual([1], solution([1], 1))

    def test_example3(self):
        self.assertEqual([], solution([], 1))