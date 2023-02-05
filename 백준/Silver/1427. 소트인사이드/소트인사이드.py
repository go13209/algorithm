import sys

num = sys.stdin.readline()

for n in sorted(num, reverse=True):
    print(n, end='')