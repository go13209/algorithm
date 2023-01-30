import sys

N = int(sys.stdin.readline())
list = [int(sys.stdin.readline()) for _ in range(N)]
list.sort()
for n in list:
    print(n)