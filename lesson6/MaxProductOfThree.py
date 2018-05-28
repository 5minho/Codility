import unittest
import functools
import operator


def solution(A):
    sorted_list = sorted(A)
    two_neg_one_pos = functools.reduce(operator.mul, sorted_list[:2] + [sorted_list[-1]])
    others = functools.reduce(operator.mul, sorted_list[-3:])
    return max(two_neg_one_pos, others)


class MaxProductOfThreeTest(unittest.TestCase):

    def test_all_components_is_negative(self):
        self.assertEqual(-2 * -3 * -1, solution([-2, -3, -1, -5]))
        self.assertEqual(-1 * -1 * -1, solution([-1, -1, -1]))

    def test_max_of_components_is_zero(self):
        self.assertEqual(0, solution([-100, -23, -496, 0]))

    def test_all_components_is_positive(self):
        self.assertEqual(4 * 4 * 3, solution([1, 3, 4, 2, 4]))

    def test_mix_positive_and_negative(self):
        self.assertEqual(-1 * -5 * 3, solution([-1, -5, 3, 2, 0]))
        self.assertEqual(-4 * -19 * 19, solution([-4, 1, 0, 6, -19, 19]))
        self.assertEqual(0, solution([-1, 0, 2]))


if __name__ == '__main__':
    unittest.main()