import unittest


def solution(K, A):
    current = 0
    result = 0
    for a in A:
        current += a
        if current >= K:
            current = 0
            result += 1
    return result


class TieRopes(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(3, solution(4, [1, 2, 3, 4, 1, 1, 3]))

    def test_example2(self):
        self.assertEqual(5, solution(5, [1, 2, 1, 1, 1, 1, 3]))

    def test_example3(self):
        self.assertEqual(1, solution(4, [5, 1, 1, 1]))

    def test_example4(self):
        self.assertEqual(4, solution(4, [5, 1, 1, 1, 1]))

    def test_example5(self):
        self.assertEqual(0, solution(5, [1, 1, 1, 1]))

    def test_example6(self):
        self.assertEqual(1, solution(2, [1, 2]))

