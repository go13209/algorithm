# 백준 10828 스택

import sys

lst = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())

    if command[0] == 'push':
        lst.append(command[1])
    elif command[0] == 'top':
        try:
            print(lst[-1])
        except:
            print(-1)
    elif command[0] == 'size':
        print(len(lst))
    elif command[0] == 'empty':
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'pop':
        try:
            print(lst.pop())
        except:
            print(-1)