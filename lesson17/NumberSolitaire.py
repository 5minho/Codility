import unittest


def solution(A):
    n = len(A)
    dp = [0] * n
    dp[0] = A[0]
    dp[1] = dp[0] + A[1]
    for i in range(2, n):
        tmp = dp[i - 1]
        for left in range(i - 2, i - 7, -1):
            if left < 0:
                break
            tmp = max(dp[left], tmp)
        dp[i] = tmp + A[i]
    return dp[n - 1]


class NumberSolitaireTests(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(8, solution([1, -2, 0, 9, -1, -2]))

    def test_example2(self):
        self.assertEqual(0, solution([0, 0, 0]))

    def test_example3(self):
        self.assertEqual(-4, solution([-1, -2, -3]))
