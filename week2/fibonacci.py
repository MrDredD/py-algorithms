# Uses python3
def calc_fib(n):
    a = 0
    b = 1
    if n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n+1): 
            c = a + b 
            a = b 
            b = c 
        return b 
n = int(input())
print(calc_fib(n))
