import unittest


def get_prime_sieve(N):
    sieve = [True] * (N + 1)
    sieve[0] = sieve[1] = False
    i = 2
    while i * i <= N:
        if sieve[i]:
            k = i * i
            while k <= N:
                sieve[k] = False
                k += i
        i += 1
    return sieve


def get_semi_prime_sieve(N):
    prime_sieve = get_prime_sieve(N)
    semi_sieve = [False] * (N + 1)
    i = 2
    while i * i <= N:
        if prime_sieve[i]:
            k = i * i
            for j in range(k, N + 1, i):
                if prime_sieve[j // i]:
                    semi_sieve[j] = True
        i += 1
    return semi_sieve


def solution(N, P, Q):
    semi_prime_sieve = get_semi_prime_sieve(N)
    prefix = [0] * (N + 1)
    for i in range(1, N + 1):
        if semi_prime_sieve[i]:
            prefix[i] = prefix[i - 1] + 1
        else:
            prefix[i] = prefix[i - 1]
    result = []
    for p, q in zip(P, Q):
        result.append(prefix[q] - prefix[p - 1])
    return result


class CountSemiprimesTests(unittest.TestCase):

    def test_prime_sieve(self):
        self.assertEqual([False, False, True, True, False, True, False, True, False, False, False], get_prime_sieve(10))
        self.assertEqual([False, False], get_prime_sieve(1))
        self.assertEqual([False, False, True], get_prime_sieve(2))
        self.assertEqual([False, False, True, True], get_prime_sieve(3))

    def test_semi_prime_sieve(self):
        self.assertEqual([False, False, False, False, True, False, True], get_semi_prime_sieve(6))
        self.assertEqual([False, False, False, False], get_semi_prime_sieve(3))
        self.assertEqual([False, False], get_semi_prime_sieve(1))
        self.assertEqual([False, False, False], get_semi_prime_sieve(2))

    def test_example1(self):
        self.assertEqual([10, 4, 0], solution(26, [1, 4, 16], [26, 10, 20]))

    def test_example2(self):
        self.assertEqual([0], solution(26, [1], [1]))

    def test_example3(self):
        self.assertEqual([0], solution(1, [1], [1]))

    def test_example4(self):
        self.assertEqual([6, 0], solution(20, [2, 1], [20, 2]))
