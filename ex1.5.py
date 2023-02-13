import time
import matplotlib.pyplot as plt

def original_code(n):
    start = time.time()
    if n == 0 or n == 1:
        return n
    else:
        result = original_code(n-1) + original_code(n-2)
    end = time.time()
    return end - start

def improved_version(n, memo={}):
    start = time.time()
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    else:
        result = improved_version(n-1, memo) + improved_version(n-2, memo)
        memo[n] = result
    end = time.time()
    return end - start

x = range(36)
y1 = [0] * 36
for i in x:
    y1[i] = original_code(i)

y2 = [0] * 36
for i in x:
    y2[i] = improved_version(i)

plt.plot(x, y1, label='Original Code')
plt.plot(x, y2, label='Improved Version')
plt.xlabel('Input: n')
plt.ylabel('Execution Time (Seconds)')
plt.title('Comparison of Original Code and Improved Version')
plt.legend()
plt.show()












