import sys

MAX = 1000000
sumOfDivisors = [1] * (MAX + 1)
for i in range(2, MAX + 1):
    for j in range(i, MAX + 1, i):
        sumOfDivisors[j] += i

prefix_sum = [0] * (MAX + 1)
for i in range(1, MAX + 1):
    prefix_sum[i] = prefix_sum[i - 1] + sumOfDivisors[i]

t = int(sys.stdin.readline().strip())

for _ in range(t):
    num = int(sys.stdin.readline().strip())
    print(prefix_sum[num])