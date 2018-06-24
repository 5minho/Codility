import unittest


def solution(A):
    A.sort()
    left, right = 0, (len(A) - 1)
    result = 2_000_000_001
    while left <= right:
        result = min(result, abs(A[left] + A[right]))
        temp_sum = A[left] + A[right]
        if temp_sum < 0:
            left += 1
        else:
            right -= 1
    return result


class MinAbsSumOfTwoTests(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(1, solution([1, 4, -3]))

    def test_example2(self):
        self.assertEqual(3, solution([-8, 4, 5, -10, 3]))
