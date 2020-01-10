# Uses python3
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    a, b = 0, 1
    n += 2
    for i in range(n % 60):
        a, b = b, (a + b) % 10
    if a == 0:
        return 9
    return a - 1


if __name__ == '__main__':    
    n = int(input())    
    print(fib(n))
