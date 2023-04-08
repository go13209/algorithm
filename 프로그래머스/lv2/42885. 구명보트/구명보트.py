from collections import deque

def solution(people, limit):
    answer = 0
    queue = deque(sorted(people))
    while queue:
        heavy = queue[-1]
        light = queue[0]
        if len(queue) == 1:
            answer += 1
            break
        if heavy + light <= limit:
            queue.pop()
            queue.popleft()
        else:
            queue.pop()
        answer += 1

    return answer