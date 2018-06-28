import unittest


def solution(S):
    stack = []
    brakets_pair = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    for braket in S:
        if braket in brakets_pair.values():
            stack.append(braket)
        else:
            if not stack or brakets_pair[braket] != stack.pop():
                return 0
    return 0 if stack else 1


class BracketsTest(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(1, solution("{{()}}"))
        self.assertEqual(0, solution("{{()}"))
        self.assertEqual(0, solution("{{()}}}"))
        self.assertEqual(0, solution("{{()]}"))
        self.assertEqual(1, solution(""))
        self.assertEqual(0, solution("}}}}]]]]]"))
        self.assertEqual(0, solution("{{{{[[[]]])))"))
        self.assertEqual(1, solution("()[]{}{}[]()"))
