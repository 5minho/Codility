import unittest
from collections import namedtuple

Fish = namedtuple('Fish', ['size', 'direction'])


def solution(A, B):
    stack = []
    for size, direction in zip(A, B):
        new_fish = Fish(size, direction)
        while stack and across(stack[-1], new_fish):
            fish = stack.pop()
            stack.append(bigger(new_fish, fish))
            new_fish = stack.pop()
        stack.append(new_fish)
    return len(stack)


def across(fish1, fish2):
    return fish1.direction == 1 and fish2.direction == 0


def bigger(fish1, fish2):
    return fish1 if fish1.size >= fish2.size else fish2


class FishTest(unittest.TestCase):

    def test_example1(self):
        A = [4, 3, 2, 1, 5]
        B = [0, 1, 0, 0, 0]
        self.assertEqual(2, solution(A, B))

    def test_example2(self):
        A = [1, 2, 3, 4, 5]
        B = [1, 1, 1, 1, 1]
        self.assertEqual(5, solution(A, B))

    def test_example3(self):
        A = [1, 2, 3, 4, 5]
        B = [0, 0, 0, 0, 0]
        self.assertEqual(5,  solution(A, B))

    def test_example4(self):
        A = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]
        B = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
        self.assertEqual(1, solution(A, B))

    def test_example5(self):
        A = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]
        B = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
        self.assertEqual(10, solution(A, B))



