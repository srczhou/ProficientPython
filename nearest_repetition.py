#!/usr/bin/env python3
import sys
import random
import string

def rand_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

# only return the min distance, not keep index
def find_nearest_repetition(paragraph):
    word_to_latest_index, nearest_repeated_distance = {}, float('inf')
    for i, word in enumerate(paragraph):
        if word in word_to_latest_index:
            nearest_repeated_distance = min(nearest_repeated_distance,
                                            i - word_to_latest_index[word])
        word_to_latest_index[word] = i
    return nearest_repeated_distance

# O(n^2) checking
def check_answer(s):
    return min([
        j - i for i, a in enumerate(s) for j, b in enumerate(s[i + 1:], i + 1)
        if a == b
    ],
               default=float('inf'))


def main():
    A = ['foo', 'bar', 'widget', 'foo', 'widget', 'widget', 'adnan']
    assert check_answer(A) == find_nearest_repetition(A)
    A = ['foo', 'bar', 'widget', 'foo', 'xyz', 'widget', 'bar', 'adnan']
    assert check_answer(A) == find_nearest_repetition(A)
    A = ['foo', 'bar', 'widget', 'adnan']
    assert check_answer(A) == find_nearest_repetition(A)
    A = []
    assert check_answer(A) == find_nearest_repetition(A)
    A = ['foo', 'foo', 'foo']
    assert check_answer(A) == find_nearest_repetition(A)
    for _ in range(10):
        n = int(sys.argv[1]) if len(sys.argv) == 2 else random.randint(1, 1000)
        s = [rand_string(random.randint(1, 10)) for _ in range(n)]
        assert check_answer(s) == find_nearest_repetition(s)


if __name__ == '__main__':
    main()
