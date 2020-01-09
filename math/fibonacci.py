"""
Computes Fibonacci sequence
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
"""
from functools import lru_cache


@lru_cache(maxsize=None)
def recursive_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)


def greedy_fibonacci(n: int) -> int:
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


def fibonacci(n: int) -> int:
    def fib(num):
        f = [[1, 1],
             [1, 0]]
        if num == 0:
            return 0
        power(f, num - 1)

        return f[0][0]

    def multiply(f, m):

        x = (f[0][0] * m[0][0] +
             f[0][1] * m[1][0])
        y = (f[0][0] * m[0][1] +
             f[0][1] * m[1][1])
        z = (f[1][0] * m[0][0] +
             f[1][1] * m[1][0])
        w = (f[1][0] * m[0][1] +
             f[1][1] * m[1][1])

        f[0][0] = x
        f[0][1] = y
        f[1][0] = z
        f[1][1] = w

    def power(f, num):
        if num == 0 or num == 1:
            return
        m = [[1, 1],
             [1, 0]]
        power(f, num // 2)
        multiply(f, f)
        if num % 2 != 0:
            multiply(f, m)

    return fib(n)


if __name__ == "__main__":
    print(fibonacci(40))

# ToDo: Add exceptions handling
# ToDo: Provide performance tests results
