#!/usr/bin/env python3
import sys
import random
import itertools
import copy

# Method naive 
def rotate_matrix_naive(square_matrix):
    matrix_size = len(square_matrix) - 1
    for i in range(len(square_matrix) // 2):
        for j in range(i, matrix_size - i):
            # Perform a 4-way exchange. Note that A[~i] for i in [0, len(A) - 1]
            # is A[-(i + 1)].
            (square_matrix[i][j],
             square_matrix[~j][i],
             square_matrix[~i][~j],
             square_matrix[j][~i]) = (square_matrix[~j][i],
                                      square_matrix[~i][~j],
                                      square_matrix[j][~i],
                                      square_matrix[i][j])

# Same algorithm, just another syntax
#def rotate_matrix(A):
#    for i in range(len(A) // 2):
#        for j in range(i, len(A) - i - 1):
#            temp = A[i][j]
#            A[i][j] = A[-1 - j][i]
#            A[-1 - j][i] = A[-1 - i][-1 - j]
#            A[-1 - i][-1 - j] = A[j][-1 - i]
#            A[j][-1 - i] = temp


# Method O(1) , but with limitation.
# the time to create object r is constant, since it simply consists of a reference to A. The time to perform reads and writes is unchanged.
# but writes to r change A
class RotatedMatrix:

    def __init__(self, square_matrix):
        self._square_matrix = square_matrix

    def read_entry(self, i, j):
        # Note that A[~i] for i in [0, len(A) - 1] is A[-(i + 1)].
        return self._square_matrix[~j][i]

    def write_entry(self, i, j, v):
        self._square_matrix[~j][i] = v



def print_matrix(A):
    for i in range(len(A)):
        print(A[i])

def check_answer(A, B):
    rA = RotatedMatrix(A)
    for i in range(len(A)):
        for j in range(len(A)):
            assert rA.read_entry(i, j) == B[i][j]


def main():
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
        k = itertools.count(1)
        A = []
        for _ in range(n):
            A.append([next(k) for _ in range(n)])
        print_matrix(A)
        B = copy.deepcopy(A)
        rotate_matrix_naive(B)
        check_answer(A, B)
        print()
        print_matrix(B)
    else:
        for _ in range(10):
            n = random.randint(1, 10)
            k = itertools.count(1)
            A = []
            for _ in range(n):
                A.append([next(k) for _ in range(n)])
            B = copy.deepcopy(A)
            rotate_matrix_naive(B)
            check_answer(A, B)


if __name__ == '__main__':
    main()
