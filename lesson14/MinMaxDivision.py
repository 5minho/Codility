import unittest


def solution(K, M, A):
    b, e = max(A), sum(A)

    def is_minimal_large(m):
        current_group_cnt = 0
        current_sum = 0
        for a in A:
            if current_sum + a > m:
                current_sum = a
                current_group_cnt += 1
            else:
                current_sum += a
            if current_group_cnt >= K:
                return False
        return True

    while b <= e:
        m = (b + e) // 2
        if is_minimal_large(m):
            e = m - 1
        else:
            b = m + 1

    return b



class MinMaxDivisionTests(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(6, solution(3, 5, [2, 1, 5, 1, 2, 2, 2]))

    def test_example2(self):
        self.assertEqual(15, solution(1, 10, [1, 2, 3, 4, 5]))

    def test_example3(self):
        self.assertEqual(10, solution(10, 10, [1, 3, 2, 6, 1, 7, 5, 4, 3, 10]))

    def test_example4(self):
        self.assertEqual(10, solution(9, 10, [1, 3, 2, 6, 1, 7, 5, 4, 3, 10]))

    def test_example5(self):
        self.assertEqual(0, solution(1, 1, [0]))
