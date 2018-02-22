import itertools
import sys
import random

def has_two_sum(A, t):
    i, j = 0, len(A) - 1

    while i <= j:
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else:  # A[i] + A[j] > t.
            j -= 1
    return False

def has_three_sum(A, t):
    A.sort()
    # Finds if the sum of two numbers in A equals to t - a.
    return any(has_two_sum(A, t - a) for a in A)


# n^3 solution.
def check_ans(A, t):
    return any(i + j + k == t for i, j, k in itertools.combinations(A, 3))


def main():
    for _ in range(10):
        n = int(sys.argv[1]) if len(sys.argv) == 2 else random.randint(1, 10000)
        T = random.randrange(n)
        A = [random.randint(-100000, 100000) for _ in range(n)]
        print(has_three_sum(A, T))
        assert check_ans(A, T) == has_three_sum(A, T)


if __name__ == '__main__':
    main()
