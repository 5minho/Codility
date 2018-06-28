import unittest


def get_peaks(A):
    n = len(A)
    peaks = [False] * n
    for i in range(1, n - 1):
        if A[i - 1] < A[i] > A[i + 1]:
            peaks[i] = True
    return peaks


def get_next_peaks(peaks):
    n = len(peaks)
    next_peak = [-1] * n
    for i in range(n - 2, -1, -1):
        if peaks[i]:
            next_peak[i] = i
        else:
            next_peak[i] = next_peak[i + 1]
    return next_peak


def solution(A):
    n = len(A)
    peaks = get_peaks(A)
    next_peaks = get_next_peaks(peaks)
    result = i = 0
    while (i - 1) * i <= n:
        num = pos = 0
        while pos < n and num < i:
            pos = next_peaks[pos]
            if pos == -1:
                break
            num += 1
            pos += i
        i += 1
        result = max(result, num)
    return result


class FlagsTests(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(3, solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]))
