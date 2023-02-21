# 백준 10866 덱

from collections import deque
import sys

lst = deque()

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    # 명령을 입력받는다.

    if command[0] == 'push_front':
        lst.appendleft(command[1])
    # 명령어가 'push_front'이면 입력받은 수를 리스트의 제일 앞에 저장한다.

    elif command[0] == 'push_back':
        lst.append(command[1])
    # 명령어가 'push_back'이면 입력받은 수를 리스트의 제일 끝에 저장한다.

    elif command[0] == 'pop_front':
        try:
            print(lst.popleft())
        except:
            print(-1)
    # 명령어가 'pop_front'이면 리스트의 제일 첫 번째 수를 pop하고 출력한다.
    # 리스트에 어떠한 요소도 없다면 -1을 출력한다.

    elif command[0] == 'pop_back':
        try:
            print(lst.pop())
        except:
            print(-1)
    # 명령어가 'pop_back'이면 리스트의 제일 마지막 수를 pop하고 출력한다.
    # 리스트에 어떠한 요소도 없다면 -1을 출력한다.

    
    elif command[0] == 'size':
        print(len(lst))
    # 명령어가 'size'이면 리스트의 길이를 출력한다.
    
    elif command[0] == 'empty':
        if lst:
            print(0)
        else:
            print(1)
    # 명령어가 'empty'이면 리스트가 비어 있을 때 1, 아니면 0을 출력한다.
    
    elif command[0] == 'front':
        try:
            print(lst[0])
        except:
            print(-1)
    # 명령어가 'front'이면 리스트의 제일 첫 번째 수를 출력한다.
    # 리스트에 어떠한 요소도 없다면 -1을 출력한다.

    elif command[0] == 'back':
        try:
            print(lst[-1])
        except:
            print(-1)
    # 명령어가 'back'이면 리스트의 제일 마지막 수를 출력한다.
    # 리스트에 어떠한 요소도 없다면 -1을 출력한다.
