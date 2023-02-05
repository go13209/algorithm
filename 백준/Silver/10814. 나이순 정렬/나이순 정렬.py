import sys

N = int(sys.stdin.readline())

lst = []

for _ in range(N):
    age, name = sys.stdin.readline().split()
    lst.append((int(age), name))

sorted_lst = sorted(lst, key = lambda x: x[0])

for age, name in sorted_lst:
    print(age, name)