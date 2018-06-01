import unittest
from operator import itemgetter
from bisect import bisect_left

LIMIT = 10000000


def solution(A):
    N = len(A)
    circles = [(i - r, i + r) for i, r in enumerate(A)]
    circles.sort(key=itemgetter(1, 0), reverse=True)
    rights = [circle[1] for circle in circles]
    rights.reverse()
    result = 0
    for i, circle in enumerate(circles):
        result += (N - bisect_left(rights, circle[0]) - (i + 1))
        if result > LIMIT:
            return -1
    return result


class NumberOfDiscIntersectionsTest(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(11, solution([1, 5, 2, 1, 4, 0]))
        self.assertEqual(0, solution([]))


if __name__ == '__main__':
    unittest.main()