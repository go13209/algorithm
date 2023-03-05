# 백준 1966 프린터 큐

from collections import deque

for _ in range(int(input())):
    N, M = map(int, input().split())
    importance = deque(list(zip(map(int, input().split()), [i for i in range(N)])))
    lst = []

    if N == 1:
        print(1)
    
    else:
        while importance:
            num, order = importance[0]
            if num < max(importance)[0]:
                importance.append(importance.popleft())
            else:
                lst.append(order)
                importance.popleft()
        else:
            print(lst.index(M) + 1)