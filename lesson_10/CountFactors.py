import unittest


def solution(N):
    num = 1
    result = 0
    while num * num < N:
        if N % num == 0:
            result += 2
        num += 1
    if num * num == N:
        result += 1
    return result


class CountFactorsTests(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(8, solution(24))

    def test_example2(self):
        self.assertEqual(1, solution(1))

    def test_example3(self):
        self.assertEqual(3, solution(4))
