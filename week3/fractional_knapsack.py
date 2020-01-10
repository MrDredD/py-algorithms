# Uses python3
import sys
from itertools import accumulate
from bisect import bisect


def frac_knapsack(vl, wt, W, n):
    """
    # >>> fracKnapsack([60, 100, 120], [10, 20, 30], 50, 3)
    240.0
    """

    r = list(sorted(zip(vl, wt), key=lambda x: x[0] / x[1], reverse=True))
    vl, wt = [i[0] for i in r], [i[1] for i in r]
    acc = list(accumulate(wt))
    k = bisect(acc, W)
    return (
        0
        if k == 0
        else sum(vl[:k]) + (W - acc[k - 1]) * (vl[k]) / (wt[k])
        if k != n
        else sum(vl[:k])
    )


def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here

    return value


from typing import List, Tuple


def fractional_knapsack(
    value: List[int], weight: List[int], capacity: int
) -> Tuple[int, List[int]]:
    """
    >>> value = [1, 3, 5, 7, 9]
    >>> weight = [0.9, 0.7, 0.5, 0.3, 0.1]
    >>> fractional_knapsack(value, weight, 5)
    (25, [1, 1, 1, 1, 1])
    >>> fractional_knapsack(value, weight, 15)
    (25, [1, 1, 1, 1, 1])
    >>> fractional_knapsack(value, weight, 25)
    (25, [1, 1, 1, 1, 1])
    >>> fractional_knapsack(value, weight, 26)
    (25, [1, 1, 1, 1, 1])
    >>> fractional_knapsack(value, weight, -1)
    (-90.0, [0, 0, 0, 0, -10.0])
    >>> fractional_knapsack([1, 3, 5, 7], weight, 30)
    (16, [1, 1, 1, 1])
    >>> fractional_knapsack(value, [0.9, 0.7, 0.5, 0.3, 0.1], 30)
    (25, [1, 1, 1, 1, 1])
    >>> fractional_knapsack([], [], 30)
    (0, [])
    """
    index = list(range(len(value)))
    ratio = [v / w for v, w in zip(value, weight)]
    index.sort(key=lambda i: ratio[i], reverse=True)

    max_value = 0
    fractions = [0] * len(value)
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity / weight[i]
            max_value += value[i] * capacity / weight[i]
            break

    return max_value, fractions


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = fractional_knapsack(values, weights, capacity)
    print("{:.4f}".format(opt_value[0]))
