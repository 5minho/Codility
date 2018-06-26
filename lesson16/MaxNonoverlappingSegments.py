import unittest


def solution(A, B):
    earliest = -1
    result = 0
    for s, e in zip(A, B):
        if earliest < s:
            result += 1
            earliest = e
    return result


class MaxNonoverlappingSegmentsTests(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(3, solution([1, 3, 7, 9, 9], [5, 6, 8, 9, 10]))

    def test_example2(self):
        self.assertEqual(1, solution([0], [0]))

    def test_example3(self):
        self.assertEqual(1, solution([0, 0], [0, 3]))

    def test_example4(self):
        self.assertEqual(3, solution([0, 1, 2], [0, 1, 2]))

    def test_example5(self):
        self.assertEqual(0, solution([], []))
