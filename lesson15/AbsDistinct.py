import unittest


def solution(A):
    return len(set([abs(a) for a in A]))


class AbsDistinctTests(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(5, solution([-5, -3, -1, 0, 3, 6]))

    def test_example2(self):
        self.assertEqual(100000, solution([-i if i % 2 == 0 else i for i in range(100000)]))
