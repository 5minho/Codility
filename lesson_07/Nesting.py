import unittest


def solution(S):
    stack = []
    for s in S:
        if s == "(":
            stack.append(s)
        else:
            if not stack or ")" == stack.pop():
                return 0
    return 0 if stack else 1


class BracketsTest(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(1, solution("(()(())())"))
        self.assertEqual(0, solution("())"))
        self.assertEqual(1, solution(""))
        self.assertEqual(0, solution("(((((("))
        self.assertEqual(0, solution("))))))"))
