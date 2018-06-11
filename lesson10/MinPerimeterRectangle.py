import unittest


def solution(N):
    result = 3000000000
    num = 1
    while num * num <= N:
        if N % num != 0:
            num += 1
            continue
        A = num
        B = N // num
        result = min(result, 2*(A+B))
        num += 1
    return result


class MinPerimeterRectangleTests(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(22, solution(30))

    def test_example2(self):
        self.assertEqual(4, solution(1))
