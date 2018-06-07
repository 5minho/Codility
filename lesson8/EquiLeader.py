import unittest


def leaders(li):
    size = 0
    value = None
    count_dict = {}
    result = []
    for i, num in enumerate(li):
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
        if size == 0:
            size += 1
            value = num
        else:
            if value == num:
                size += 1
            else:
                size -= 1
        result.append(value if count_dict[value] > ((i + 1) // 2) else None)
    return result


def solution(A):
    n = len(A)
    leaders_li = leaders(A)
    r_leaders_li = list(reversed(leaders(reversed(A))))
    return sum(1 for i in range(n - 1) if leaders_li[i] is not None and leaders_li[i] == r_leaders_li[i + 1])


class EquiLeaderTests(unittest.TestCase):

    def test_leader_context(self):
        self.assertListEqual([4, None, 4, 4, 4, 4], list(leaders([4, 3, 4, 4, 4, 2])))
        self.assertListEqual([2, None, 4, 4, 4, 4], list(leaders([2, 4, 4, 4, 3, 4])))

    def test_example1(self):
        self.assertEqual(2, solution([4, 3, 4, 4, 4, 2]))

    def test_example2(self):
        self.assertEqual(0, solution([1, 2, 3, 4, 5, 6]))

    def test_example3(self):
        self.assertEqual(0, solution([6, 5, 4, 3, 2, 1]))

    def test_example4(self):
        self.assertEqual(0, solution([3, 3, 3, 4, 4, 4]))

    def test_example5(self):
        self.assertEqual(5, solution([1, 1, 1, 1, 1, 1]))

    def test_example5(self):
        self.assertEqual(0, solution([1]))
