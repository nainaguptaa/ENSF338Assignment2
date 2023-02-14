import timeit
x  = {}
def memo(n):
    if n == 0 or n == 1:
        return n
    if n in x:
        return x[n]

    else:

        x[n] =  memo(n-1) + memo(n-2)
        return x[n]
