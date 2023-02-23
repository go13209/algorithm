from collections import deque

def solution(priorities, location):
    doc = deque(list(enumerate(priorities)))
    order = []

    while doc:
        if doc[0][1] < max(priorities):
            doc.append(doc.popleft())
        else:
            order.append(doc.popleft())
            priorities.remove(max(priorities))

    order = dict(order)
    answer = list(order.keys()).index(location) + 1
    
    return answer