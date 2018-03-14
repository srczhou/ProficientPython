#!/usr/bin/env python3
import math
import sys
import random


def power_x_y(x, y):
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0 / x
    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1
    return result


def main():
    if len(sys.argv) == 3:
        x, y = float(sys.argv[1]), int(sys.argv[2])
        print('%g^%d: %g, %g' % (x, y, power_x_y(x, y), x**y))
        assert math.isclose(power_x_y(x, y), x**y)
    else:
        for _ in range(100):
            x, y = random.uniform(0.0, 10.0), random.randint(-32, 32)
            print('%g^%d: %g, %g' % (x, y, power_x_y(x, y), x**y))
            assert math.isclose(power_x_y(x, y), x**y)


if __name__ == '__main__':
    main()
