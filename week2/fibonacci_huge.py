# Uses python3
from functools import lru_cache
@lru_cache(maxsize=None)
def fib4(n,mod):
    if n <= 1:
        return n

    if n%2:
        m = (n+1)//2
        return (fib4(m, mod) ** 2 + fib4(m - 1, mod) ** 2) % mod
    else:
        m = n//2
        return ((2*fib4(m - 1, mod) + fib4(m, mod)) * fib4(m, mod)) % mod

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fib4(n, m))
