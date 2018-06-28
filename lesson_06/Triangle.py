import unittest


def solution(A):
    N = len(A)
    A = sorted(A)
    for i in range(N - 2):
        if is_triangular(A[i], A[i + 1], A[i + 2]):
            return 1
    return 0


def is_triangular(a, b, c):
    return a + b > c and b + c > a and c + a > b


class Triangle(unittest.TestCase):

    def test_below_three_components(self):
        self.assertEqual(0, solution([1, 2]))
        self.assertEqual(0, solution([1]))

    def test_three_components(self):
        self.assertEqual(1, solution([2, 4, 3]))

    def test_only_positive(self):
        self.assertEqual(1, solution([10, 2, 5, 1, 8, 20]))

    def test_sequence(self):
        self.assertEqual(1, solution([1, 1, 1, 1, 5, 5, 5]))


if __name__ == '__main__':
    unittest.main()
