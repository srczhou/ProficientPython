#!/usr/bin/env python3
import sys
import random
import itertools

# method 1
def matrix_in_spiral_order0(square_matrix):
    def matrix_layer_in_clockwise(offset):
        if offset == len(square_matrix) - offset - 1:
            # square_matrix has odd dimension, and we are at the center of the
            # matrix square_matrix.
            spiral_ordering.append(square_matrix[offset][offset])
            return

        # list(zip(*2dlist)) is like transpose, make sure use "*" (unpacks)
        spiral_ordering.extend(square_matrix[offset][offset:-1 - offset])
        spiral_ordering.extend(
            list(zip(*square_matrix))[-1 - offset][offset:-1 - offset])
        spiral_ordering.extend(
            square_matrix[-1 - offset][-1 - offset:offset:-1])
        spiral_ordering.extend(
            list(zip(*square_matrix))[offset][-1 - offset:offset:-1])

    spiral_ordering = []
    for offset in range((len(square_matrix) + 1) // 2):
        matrix_layer_in_clockwise(offset)
    return spiral_ordering

# method 2
def matrix_in_spiral_order(square_matrix):
    SHIFT = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = x = y = 0
    spiral_ordering = []

    for _ in range(len(square_matrix)**2):
        spiral_ordering.append(square_matrix[x][y])
        square_matrix[x][y] = 0
        next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        if (next_x not in range(len(square_matrix)) or next_y not in range(
                len(square_matrix)) or square_matrix[next_x][next_y] == 0):
            direction = (direction + 1) & 3
            next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        x, y = next_x, next_y
    return spiral_ordering


def print_matrix_in_spiral_order2(A):
    shift = (1, 1, -1, -1)  # step size for each direction
    limits = [len(A) - 1, len(A) - 1, 0,
              1]  # need to change direction at this point
    xy = [0, 0]  # x and y coordinates
    x_or_y = 1  # which coordinate changes now
    d = 0

    for i in range(len(A)**2):
        print(A[xy[0]][xy[1]], end=' ')
        if xy[x_or_y] == limits[d]:  # at the last point in this direction
            limits[d] -= shift[d]  # one row/column less next time
            d = (d + 1) & 3
            x_or_y = 1 - x_or_y  # change other coordinate from now on
        xy[x_or_y] += shift[d]


def simple_test():
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert matrix_in_spiral_order0(A) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert matrix_in_spiral_order(A) == [1, 2, 3, 6, 9, 8, 7, 4, 5]


def main():
    simple_test()
    N = int(sys.argv[1]) if len(sys.argv) == 2 else random.randint(1, 50)
    k = itertools.count(1)
    A = [[next(k) for _ in range(N)] for _ in range(N)]
    print_matrix_in_spiral_order2(A)
    print()
    print(matrix_in_spiral_order0(A))
    print(matrix_in_spiral_order(A))


if __name__ == '__main__':
    main()
