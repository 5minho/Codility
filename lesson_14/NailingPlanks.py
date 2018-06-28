import unittest
from operator import itemgetter


def solution(A, B, C):
    nail_info = sorted(enumerate(C), key=itemgetter(1))

    def bisearch(plank):
        b, e = 0, (len(nail_info) - 1)
        idx, pos = -1, -1
        while b <= e:
            m = (b + e) // 2
            if nail_info[m][1] < plank[0]:
                b = m + 1
            elif nail_info[m][1] > plank[1]:
                e = m - 1
            else:
                e = m - 1
                idx = nail_info[m][0]
                pos = m
        return idx, pos

    def get_max_idx(plank, previous_max_idx):
        idx, pos = bisearch(plank)
        if idx == -1:
            raise Exception
        pos += 1
        while pos < len(nail_info) and nail_info[pos][1] <= plank[1]:
            idx = min(nail_info[pos][0], idx)
            if idx <= previous_max_idx:
                return previous_max_idx
            pos += 1
        return idx

    planks = zip(A, B)
    max_idx = 0

    for plank in planks:
        try:
            max_idx = max(max_idx, get_max_idx(plank, max_idx))
        except Exception as e:
            return -1
    return max_idx + 1


class NailingPlanksTests(unittest.TestCase):

    def test_sort(self):
        A = [5, 2, 1, 7]
        B = [9, 5, 9, 10]
        self.assertEqual([(1, 9), (2, 5), (5, 9), (7, 10)], sorted(zip(A, B), key=itemgetter(0)))
        self.assertEqual([(2, 5), (5, 9), (1, 9), (7, 10)], sorted(zip(A, B), key=itemgetter(1)))

    def test_example1(self):
        A = [1, 4, 5, 8]
        B = [4, 5, 9, 10]
        C = [4, 6, 7, 10, 2]
        self.assertEqual(4, solution(A, B, C))

    def test_example2(self):
        A = [5, 2, 1, 7]
        B = [9, 5, 9, 10]
        C = [4, 6, 7, 10, 2]
        self.assertEqual(3, solution(A, B, C))
