import unittest


def hit(cache, num):
    return num in cache


# slow(66%)
# def solution(A):
#     sorted_desc = sorted(A, reverse=True)
#     outer_cache = {}
#     outer_cache.get()
#     for i, a in enumerate(sorted_desc):
#         if hit(outer_cache, a):
#             continue
#         outer_cache[a] = i
#         for d in sorted_desc[i + 1:]:
#             if a % d != 0:
#                 outer_cache[a] += 1
#     return [outer_cache[a] for a in A]


# fast(88%)
# def solution(A):
#     n = len(A)
#     count = {}
#     result = []
#     cache = {}
#     for a in A:
#         if a in count:
#             count[a] += 1
#         else:
#             count[a] = 1
#     for a in A:
#         if hit(cache, a):
#             result.append(cache[a])
#             continue
#         i = 1
#         d = 0
#         while i * i <= a:
#             if a % i == 0:
#                 d += count.get(i, 0)
#                 if a // i != i:
#                     d += count.get(a // i, 0)
#             i += 1
#         result.append(n - d)
#         cache[a] = n - d
#     return result

# golden(100%)
def solution(A):
    n = len(A)
    max_input = max(A)
    count = {}
    for a in A:
        if a in count:
            count[a] += 1
        else:
            count[a] = 1
    divisors = {}
    for a in A:
        divisors[a] = set([1, a])
    divisor = 2
    while divisor * divisor <= max_input:
        i = divisor
        while i <= max_input:
            if i in divisors and divisor not in divisors[i]:
                divisors[i].add(divisor)
                divisors[i].add(i // divisor)
            i += divisor
        divisor += 1
    result = []
    for a in A:
        result.append(n - sum(count.get(divisor, 0) for divisor in divisors[a]))
    return result


class CountNonDivisibleTests(unittest.TestCase):

    def test_array_slice(self):
        self.assertEqual([1, 2, 3, 4], [1, 2, 3, 4, 5][:-1])

    def test_sorted(self):
        self.assertEqual([6, 3, 3, 2, 1], sorted([3, 1, 2, 3, 6], reverse=True))

    def test_example1(self):
        self.assertEqual([2, 4, 3, 2, 0], solution([3, 1, 2, 3, 6]))

    def test_example2(self):
        self.assertEqual([0, 0, 0, 0, 0], solution([1, 1, 1, 1, 1]))

    def test_example3(self):
        self.assertEqual([0, 0], solution([1, 1]))
