import unittest


def sieve_for_factor(N):
    sieve = [0] * (N + 1)
    i = 2
    while i * i <= N:
        k = i * i
        if sieve[k] == 0:
            while k <= N:
                sieve[k] = i
                k += i
        i += 1
    return sieve


# Memory Error (61%)
# def solution(A, B):
#     sieve = sieve_for_factor(max(max(A), max(B)))
#
#     def prime_set(A):
#         result = set()
#         num = A
#         while sieve[num] != 0:
#             result.add(sieve[num])
#             num //= sieve[num]
#         if num != 1:
#             result.add(num)
#         return result
#
#     return sum(1 for a, b in zip(A, B) if prime_set(a) == prime_set(b))

def gcd(n, m):
    mod = n % m
    return gcd(m, mod) if mod != 0 else m


def equal_prime_factor(n, m):
    n_m_gcd = gcd(n, m)
    for q in (n, m):
        while q != 1:
            n_m_q_gcd = gcd(q, n_m_gcd)
            if n_m_q_gcd == 1:
                return False
            q //= n_m_q_gcd
    return True


def solution(A, B):
    return sum(1 for a, b in zip(A, B) if equal_prime_factor(a, b))


class CommonPrimeDivisorsTests(unittest.TestCase):

    def test_gcd(self):
        self.assertEqual((2**5*3**6*5*7**3*11**3)/(2*3*5*7**3), 2**4*3**5*11**3)
        # self.assertEqual(2, gcd(2**4 * 3**5 * 11**3, 2*3*5*7**3))

    def test_example1(self):
        self.assertEqual(1, solution([15, 10, 3], [75, 30, 5]))

    def test_example2(self):
        self.assertEqual(1, solution([1], [1]))

    def test_example3(self):
        self.assertEqual(1, solution([1, 3], [1, 5]))

    def test_example4(self):
        self.assertEqual(2, solution([6059, 551], [442307, 303601]))

    def test_example5(self):
        self.assertEqual(1, solution([9, 3, 1], [1, 3, 9]))

    def test_example6(self):
        self.assertEqual(0, solution([9], [16]))



