from collections import deque

def solution(my_string):
    lst = deque(my_string.split())
    answer = int(lst.popleft())
    while lst:
        if lst.popleft() == '+':
            num = int(lst.popleft())
            answer += num
        else:
            num = int(lst.popleft())
            answer -= num
    return answer