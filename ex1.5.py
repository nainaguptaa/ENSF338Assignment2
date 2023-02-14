import timeit
import matplotlib.pyplot as plt

def func(n):
    if n== 0 or n==1:
        return n
    else:
        return func(n-1)+func(n-2)

x  = {}
def memo(n):
    if n == 0 or n == 1:
        return n
    if n in x:
        return x[n]
    else:
        x[n] =  memo(n-1) + memo(n-2)
        return x[n]

times_func = []
times_memo = []

for i in range(36):
    t = timeit.timeit(lambda: func(i), number=1)
    times_func.append(t)
    t = timeit.timeit(lambda: memo(i), number=1)
    times_memo.append(t)

plt.plot(range(36), times_func, label="func")
plt.plot(range(36), times_memo, label="memo")
plt.legend()
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.show()
