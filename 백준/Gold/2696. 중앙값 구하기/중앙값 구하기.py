# 백준 2696 중앙값 구하기

import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    M = int(sys.stdin.readline())
    lst = []
    answer = []

    for _ in range(M//10 + 1):
        nums = deque(list(map(int, sys.stdin.readline().split())))

        for i in range(len(nums)):
            if i % 2 == 0:
                lst.append(nums.popleft())
                lst.sort()
                answer.append(lst[len(lst)//2])
            else:
                lst.append(nums.popleft())
    
    start = 0
    end = 10
    if len(answer) > 10:
        print(len(answer))
        for _ in range(len(answer)//10):
            print(*answer[start:end])
            start += 10
            end += 10
        else:
            print(*answer[start:])
    else:
        print(len(answer))
        print(*answer)
