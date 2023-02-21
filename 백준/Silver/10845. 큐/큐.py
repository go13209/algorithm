# 백준 10845 큐

from collections import deque
import sys

lst = deque()

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())

    if command[0] == 'push':
        lst.append(command[1])
    
    elif command[0] == 'pop':
        try:
            print(lst.popleft())
        except:
            print(-1)
    
    elif command[0] == 'size':
        print(len(lst))
    
    elif command[0] == 'empty':
        if lst:
            print(0)
        else:
            print(1)
    
    elif command[0] == 'front':
        try:
            print(lst[0])
        except:
            print(-1)

    elif command[0] == 'back':
        try:
            print(lst[-1])
        except:
            print(-1)
