"""Remember that a fibonacci sequence: 0,1,1,2,3,5,8,13,21,... starts 
off with a base case checking to see if n = 0 or 1, then it returns 1.
Else it returns fib(n-1)+fib(n+2)."""

def fibo(n):

    if n == 1 or n == 0:
        return n

    else:
        return(fibo(n-1) + fibo(n-2))
    

print(fibo(10)) 