import unittest


def solution(A):
    n = len(A)
    A.sort()
    result = 0
    for x in range(n):
        z = x + 2
        for y in range(x + 1, n):
            while z < n and A[x] + A[y] > A[z]:
                z += 1
            result += z - y - 1
    return result


class CountTrianglesTests(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(4, solution([10, 2, 5, 1, 8, 12]))

    def test_example2(self):
        self.assertEqual(0, solution([1, 2]))

