#!/usr/bin/env python3
import sys
import random

RED, WHITE, BLUE = range(3)

# 1. slow inplace, O(n^2), additional space complexity is O(1)
def dutch_flag_partition1(pivot_index, A):
    pivot = A[pivot_index]
    # First pass: group elements smaller than pivot.
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break
    # Second pass: group elements larger than pivot.
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        # Look for a larger element. Stop when we reach an element less than
        # pivot, since first pass has moved them to the start of A.
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break

# 2. O(n), space O(1)
def dutch_flag_partition2(pivot_index, A):
    pivot = A[pivot_index]
    # First pass: group elements smaller than pivot.
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    # Second pass: group elements larger than pivot.
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1

# 3. single pass. O(n), space O(1)
def dutch_flag_partition3(pivot_index, A):
    pivot = A[pivot_index]
    # Keep the following invariants during partitioning:
    # bottom group: A[:smaller].
    # middle group: A[smaller:equal].
    # unclassified group: A[equal:larger].
    # top group: A[larger:].
    smaller, equal, larger = 0, 0, len(A)
    # Keep iterating as long as there is an unclassified element.,
    while equal < larger:
        # A[equal] is the incoming unclassified element.
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:  # A[equal] > pivot.
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]


def main():
    for _ in range(1000):
        n = int(sys.argv[1]) if len(sys.argv) == 2 else random.randint(1, 100)
        A = [random.randint(0, 2) for _ in range(n)]
        pivot_index = random.randrange(n)
        pivot = A[pivot_index]
        print("*** pivot=", pivot, "original list=", A)
        dutch_flag_partition3(pivot_index, A)
        i = 0
        while i < len(A) and A[i] < pivot:
            print(A[i], end=' ')
            i += 1
        while i < len(A) and A[i] == pivot:
            print(A[i], end=' ')
            i += 1
        while i < len(A) and A[i] > pivot:
            print(A[i], end=' ')
            i += 1
        print()
        assert i == len(A)


if __name__ == '__main__':
    main()
