# Uses python3
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n, m):
    a, b = 0, 1
    m += 2
    n += 1
    mem = 0
    for i in range(n % 60):
        a, b = b, (a + b) % 10
    mem = a
    #print(mem - 1)
    a, b = 0, 1
    for i in range(m % 60):
        a, b = b, (a + b) % 10 
    #print(a)
    return (10 + a - mem) % 10


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fib(n, m))