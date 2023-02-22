from collections import deque

def solution(arr):
    arr = deque(arr)
    answer = []
    answer.append(arr.popleft())
    
    while arr:
        if arr[0] == answer[-1]:
            arr.popleft()
        else:
            answer.append(arr.popleft())
    return answer