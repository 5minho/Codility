import unittest


def solution(N, M):
    def gcd(a, b):
        mod = a % b
        return gcd(b, mod) if mod != 0 else b
    return N / gcd(N, M)


class ChocolatesByNumbers(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(5, solution(10, 4))

    def test_example2(self):
        self.assertEqual(1, solution(1, 1))

    def test_example3(self):
        self.assertEqual(1, solution(1, 1000000))

    def test_example4(self):
        self.assertEqual(1, solution(4, 1000000))
