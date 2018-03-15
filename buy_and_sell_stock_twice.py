#!/usr/bin/env python3
import math
import random
import sys

# enumerate(A[1:],1) the second 1 means the index start from 1
# because of the slice, the first item in A is excluded, you need the start=1
# so the index is the same as the index of A.
def buy_and_sell_stock_twice(prices):
    max_total_profit, min_price_so_far = 0.0, float('inf')
    first_buy_sell_profits = [0] * len(prices)
    # Forward phase. For each day, we record maximum profit if we sell on that
    # day. (Could be 0, which means buy and sell once is the best solution.)
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_sell_profits[i] = max_total_profit

    # Backward phase. For each day, find the maximum profit if we make the
    # second buy on that day. (Also could be 0)
    max_price_so_far = float('-inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(max_total_profit, max_price_so_far - price +
                               first_buy_sell_profits[i - 1])
    return max_total_profit

# O(n) timing, and O(1) space
# Equivalent to the following (the sequence just assure non-blocking assignment)
#  max_profits[1] = max(<itself>, price - min_prices[1])
#  min_prices[1] = min(<itself>, price - max_profits[0])
#  max_profits[0] = max(<itself>, price - min_prices[0])
#  min_prices[0] = min(<itself>, price)
# The min_prices is the cost, max_profits is the profit,
#  The 1st buy's cost is just the price,
#  the 2nd buy's cost is price - 1st buy's profit.
#  the 1st buy's profit is current price -1st buy's cost
#  the 2nd buy's profit is current price -2nd buy's cost
# The final result (the return value) is max_profits[1]
def buy_and_sell_stock_twice_constant_space(prices):
    min_prices, max_profits = [float('inf')] * 2, [0] * 2
    for price in prices:
        for i in reversed(list(range(2))):
            max_profits[i] = max(max_profits[i], price - min_prices[i])
            min_prices[i] = min(min_prices[i],
                                price - (0 if i == 0 else max_profits[i - 1]))
    return max_profits[-1]


def main():
    for _ in range(1000):
        n = int(sys.argv[1]) if len(sys.argv) == 2 else random.randint(1, 100)
        a = [random.uniform(0, 10000) for _ in range(n)]
        assert math.isclose(
            buy_and_sell_stock_twice_constant_space(a),
            buy_and_sell_stock_twice(a))


if __name__ == '__main__':
    main()
