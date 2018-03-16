#!/usr/bin/env python3
import itertools

# Every permutation can be represented by a collection of independent
# permutations, each of which is cyclic.

# method 1
def apply_permutation(perm, A):
    for i in range(len(A)):
        # Check if the element at index i has not been moved by checking if
        # perm[i] is nonnegative.
        next = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]
            # Subtracts len(perm) from an entry in perm to make it negative,
            # which indicates the corresponding move has been performed.
            perm[next] -= len(perm)
            next = temp
    # Restore perm.
    perm[:] = [a + len(perm) for a in perm]
# If cannot use the sign bit, use array of boolean to record if it's processed


# method 2
def apply_permutation2(perm, A):
    def cyclic_permutation(start, perm, A):
        i, temp = start, A[start]
        while True:
            next_i = perm[i]
            next_temp = A[next_i]
            A[next_i] = temp
            i, temp = next_i, next_temp
            if i == start:
                break
    for i in range(len(A)):
        # Traverses the cycle to see if i is the minimum element.
        j = perm[i]
        while j != i:
            if j < i:
                break           # jump out of while loop without run else block
            j = perm[j]
        else:                   # else won't run if hit the break
            cyclic_permutation(i, perm, A)

def main():
    for per in itertools.permutations([0, 1, 2, 3, 4]):
        perm = list(per)
        print("perm = ", perm)
        A1 = ['a', 'b', 'c', 'd', 'e']
        apply_permutation(perm, A1)
        print("  ", A1)
        # Note: cannot use A1 = A2 = ['a', ..., 'e'], change A1 will change A2
        A2 = ['a', 'b', 'c', 'd', 'e']
        apply_permutation2(perm, A2)
        assert A1 == A2

if __name__ == '__main__':
    main() 
