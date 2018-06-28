import unittest


def solution(A):
    A.append(1)
    MAX_N = 100000
    N = len(A)
    fibo = [1, 1]

    for i in range(2, MAX_N):
        f = fibo[i - 1] + fibo[i - 2]
        if f > N:
            break
        fibo.append(f)

    dp = [-1] * N
    for f in fibo:
        if A[f - 1] == 1:
            dp[f - 1] = 1

    for i, a in enumerate(A):
        if a == 0 or dp[i] != -1:
            continue
        min_idx = -1
        pre_jump_cnt = 100000
        for f in fibo:
            pre_idx = i - f
            if pre_idx < 0:
                break
            if dp[pre_idx] != -1 and pre_jump_cnt > dp[pre_idx]:
                min_idx = pre_idx
                pre_jump_cnt = dp[pre_idx]
        if min_idx != -1:
            dp[i] = dp[min_idx] + 1

    return dp[N - 1]


class FibFrogTests(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(3, solution([0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]))

    def test_example2(self):
        self.assertEqual(1, solution([0, 1]))

    def test_example3(self):
        self.assertEqual(-1, solution([0, 0, 0]))

    def test_example4(self):
        self.assertEqual(1, solution([0, 0, 0, 0]))

    def test_example5(self):
        self.assertEqual(1, solution([1, 1, 1, 1]))