import unittest

def solution(A):
    return len(set(A))


class DistinctTest(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(3, solution([3, 2, 1, 3, 1, 1, 2]))


if __name__ == '__main__':
    unittest.main()

