import unittest


def solution(A):
    appears = set()
    for a in A:
        if a in appears:
            appears.remove(a)
        else:
            appears.add(a)
    return appears.pop()


class OddOccurrencesInArrayTests(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(7, solution([9, 3, 9, 3, 9, 7, 9]))

    def test_example2(self):
        self.assertEqual(3, solution([1, 2, 1, 2, 3]))

    def test_example3(self):
        self.assertEqual(1, solution([1]))