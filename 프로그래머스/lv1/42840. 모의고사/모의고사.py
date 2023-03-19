from collections import deque

def solution(answers):
    student_1 = deque([1, 2, 3, 4, 5])
    student_2 = deque([2, 1, 2, 3, 2, 4, 2, 5])
    student_3 = deque([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    
    answer = []
    scores = [0, 0, 0]
    
    for i in answers:
        num_1 = student_1.popleft()
        if num_1 == i:
            scores[0] += 1
        student_1.append(num_1)

        num_2 = student_2.popleft()
        if num_2 == i:
            scores[1] += 1
        student_2.append(num_2)

        num_3 = student_3.popleft()
        if num_3 == i:
            scores[2] += 1
        student_3.append(num_3)

    for i in range(3):
        if scores[i] == max(scores):
            answer.append(i + 1)
            
    return answer