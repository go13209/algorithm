# 백준 1920 수 찾기

import sys

N = int(sys.stdin.readline())
N_nums = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_nums = list(map(int, sys.stdin.readline().split()))

for m in M_nums:
    if m in N_nums:
        print(1)
    else:
        print(0)
