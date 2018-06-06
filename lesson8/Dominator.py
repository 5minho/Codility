import unittest


def solution(A):
    size = 0
    value = None
    idx = 0
    for i, num in enumerate(A):
        if size == 0:
            size += 1
            value = num
            idx = i
            continue
        if value == num:
            size += 1
        else:
            size -= 1
    if size == 0:
        return -1
    occurs = sum(1 for num in A if num == value)
    return idx if occurs > (len(A) // 2) else -1


class DominatorTests(unittest.TestCase):

    def test_example1(self):
        self.assertIn(solution([3, 4, 3, 2, 3, -1, 3, 3]), [0, 2, 4, 6, 7])

    def test_example2(self):
        self.assertEqual(-1, solution([]))

    def test_example3(self):
        self.assertIn(solution([-1, 2, 3, 2]), [-1])

    def test_example4(self):
        self.assertIn(solution([-1, 2, 3, 2, 3, 3]), [-1])

    def test_example5(self):
        self.assertIn(solution([1, 1, 2, 2, 3, 3]), [-1])

    def test_example6(self):
        self.assertIn(solution([2, 2, 2, 2, 0, 0, 0]), [0, 1, 2, 3])

    def test_example7(self):
        self.assertIn(solution([0, 0, 0, 2, 2, 2, 2]), [3, 4, 5, 6])

    def test_example8(self):
        self.assertIn(solution([0, 0, 0, 2, 2, 2]), [-1])

    def test_example9(self):
        self.assertIn(solution([2, 1, 1, 3]), [-1])
