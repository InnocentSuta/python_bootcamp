
def fac(x):

    if x <= 1:
        return 1
    else:
        return fac(x - 1) * x

x = fac(5)

print(x)

 #writing the recursive fibonacci sequence

def fib(n):
    if n <= 1:
        return n
    else:
        return fib( n - 1 ) + fib( n - 2 )

print( fib(30) ) # results in 5