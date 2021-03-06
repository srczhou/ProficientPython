#!/usr/bin/env python3
import sys
import random

# prime_sieve_basic
def generate_primes(n):
    primes = []
    # is_prime[p] represents if p is prime or not. Initially, set each to
    # true, expecting 0 and 1. Then use sieving to eliminate nonprimes.
    is_prime = [False, False] + [True] * (n - 1)
    for p in range(2, n):
        if is_prime[p]:
            primes.append(p)
            # Sieve p's multiples.
            for i in range(p, n + 1, p):
                is_prime[i] = False
    return primes


# Given n, return all primes up to and including n.
# Compare the basic sieve algorithm
#  1. sieving p's multiples from p^2 instead of p
#  2. reduce storage by ignoring even numbers
def generate_primes_from_1_to_n(n):
    size = (n - 3) // 2 + 1
    primes = [2]  # Stores the primes from 1 to n.
    # is_prime[i] represents (2i + 3) is prime or not.
    # Initially set each to true. Then use sieving to eliminate nonprimes.
    is_prime = [True] * size
    for i in range(size):
        if is_prime[i]:
            p = i * 2 + 3
            primes.append(p)
            # Sieving from p^2, where p^2 = (4i^2 + 12i + 9). The index in is_prime
            # is (2i^2 + 6i + 3) because is_prime[i] represents 2i + 3.
            #
            # Note that we need to use long for j because p^2 might overflow.
            for j in range(2 * i**2 + 6 * i + 3, size, p):
                is_prime[j] = False
    return primes


def main():
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
        print('n =', n)
        primes = generate_primes_from_1_to_n(n)
        print(*primes, sep='\n')
        return all(i % j for i in primes for j in range(2, i))
    else:
        for _ in range(100):
            n = random.randint(2, 100000)
            print('n =', n)
            primes = generate_primes_from_1_to_n(n)
            return all(i % j for i in primes for j in range(2, i))


if __name__ == '__main__':
    main()
