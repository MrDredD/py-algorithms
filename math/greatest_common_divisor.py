"""
Greatest Common Divisor.
"""


def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def gcd(a: int, b: int) -> int:
    return greatest_common_divisor(a, b)