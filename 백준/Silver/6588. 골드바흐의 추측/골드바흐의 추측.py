import sys

MAX = 1000000
check = [False, False] + [True] * (MAX - 1)
primes = []

for i in range(2, MAX + 1):
    if check[i]:
        primes.append(i)
        for j in range(2 * i, MAX + 1, i):
            check[j] = False

while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break
    for p in primes:
        if check[n - p]:
            print(f"{n} = {p} + {n - p}")
            break
