import unittest

MAX = 1000000000
# total 70%, Correctness : 100%, Performance : 40%
# def solution(M, A):
#     n = len(A)
#     result = 0
#     for x in range(n):
#         slice_set = set([A[x]])
#         y = x + 1
#         while y < n and A[y] not in slice_set:
#             slice_set.add(A[y])
#             y += 1
#         result += (y - x)
#         if result >= MAX:
#             return MAX
#     return result


# total 100%, Correctness : 100%, Performance : 100%
def solution(M, A):
    seen = [False] * (M + 1)
    n = len(A)
    result = left = right = 0
    while left < n and right < n:
        if not seen[A[right]]:
            result += (right - left + 1)
            if result >= MAX:
                return MAX
            seen[A[right]] = True
            right += 1
        else:
            seen[A[left]] = False
            left += 1
    return result


class CountDistinctSlicesTests(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(9, solution(6, [3, 4, 5, 5, 2]))

    def test_example2(self):
        self.assertEqual(6, solution(10, [1, 1, 1, 1, 1, 1]))

    def test_example3(self):
        self.assertEqual(21, solution(10, [2, 5, 9, 5, 2, 0, 0, 1, 2]))
