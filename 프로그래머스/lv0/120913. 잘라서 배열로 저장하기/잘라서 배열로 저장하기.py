from collections import deque

def solution(my_str, n):
    string = deque(my_str)
    result = ''
    answer = []
    cnt = 0
    while string:
        if cnt == n:
            answer.append(result)
            result = ''
            cnt = 0
        result += string.popleft()
        cnt += 1
    else:
        answer.append(result)
        
    return answer