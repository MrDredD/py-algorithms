# Uses python3
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    a, b = 0, 1
    for i in range(n % 60):
        a, b = b, (a + b) % 10
    
    return (a*b) % 10

if __name__ == '__main__':
    n = int(input())    
    print(fib(n))
