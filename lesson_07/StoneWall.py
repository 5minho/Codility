import unittest


def solution(H):
    blocks = 0
    stack = []
    for h in H:
        while stack and stack[-1] > h:
            stack.pop()
        if not stack or stack[-1] != h:
            blocks += 1
            stack.append(h)
    return blocks


class StoneWallTest(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(7, solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))
        self.assertEqual(3, solution([3, 2, 1]))
        self.assertEqual(3, solution([1, 2, 3]))
        self.assertEqual(1, solution([1]))
        self.assertEqual(3, solution([1, 2, 3, 3, 2, 1]))


if __name__ == '__main__':
    unittest.main()