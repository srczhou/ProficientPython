#!/usr/bin/env python3

# 1. brute-force, time complexity O(n)
def parity1(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

# 2. skip consecutive 0s
def parity2(x):
    result = 0
    while x:
        x &= x - 1  # x&(x-1) drop the lowest set bit of x
        result ^= 1
    return result

# 3. lookup table, O(n/L)
PRECOMPUTED_PARITY = [parity1(i) for i in range(1 << 16)]
def parity3(x):
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    return (PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)] ^
            PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & BIT_MASK] ^
            PRECOMPUTED_PARITY[(x >> MASK_SIZE) & BIT_MASK] ^
            PRECOMPUTED_PARITY[x & BIT_MASK])

# 4. using associativity, divide by half each time, O(logn)
def parity4(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1

for i in [0, 1, 2, 5, 1222, 343466, 595959995959]:
    print(parity1(i), parity2(i), parity3(i), parity4(i)) 

# 3 and 4 assume 64-bit number, but python3 integer has unlimited precision, so
# for i = 1 << 70, 3 get list index out of range error, 4 get wrong results.

