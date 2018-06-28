import unittest


def get_peak_indies(A):
    n = len(A)
    peaks = []
    for i in range(1, n - 1):
        if A[i - 1] < A[i] > A[i + 1]:
            peaks.append(i)
    return peaks


def solution(A):
    n = len(A)
    peak_indies = get_peak_indies(A)
    result = 0
    for block_cnt in range(len(peak_indies), 0, -1):
        if n % block_cnt != 0:
            continue
        block_size = n // block_cnt
        found = [False] * block_cnt
        num = 0
        for peak_idx in peak_indies:
            block_idx = peak_idx // block_size
            if not found[block_idx]:
                found[block_idx] = True
                num += 1
            if num == block_cnt:
                return num
    return result


class PeaksTests(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(3, solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]))

    def test_example2(self):
        self.assertEqual(3, solution([0, 1, 0, 4, 0, 2, 0, 3, 0]))

    def test_example3(self):
        self.assertEqual(0, solution([1, 1, 1, 1, 1, 1, 1, 1, 1]))

    def test_example4(self):
        self.assertEqual(0, solution([1]))

    def test_example5(self):
        self.assertEqual(2, solution([0, 1, 0, 1, 0, 1, 0, 0]))
