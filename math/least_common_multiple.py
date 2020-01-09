"""
Computes least common multiple of two given integers
"""


def least_common_multiple(a: int, b: int) -> int:
    maximum = max(a, b)
    result = maximum
    while (result % a > 0) or (result % b > 0):
        result += maximum
    return result


def lcm(a: int, b: int) -> int:
    return least_common_multiple(a, b)