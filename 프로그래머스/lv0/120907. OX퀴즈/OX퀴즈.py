def solution(quiz):
    answer = []
    for q in quiz:
        lst = q.split()
        if lst[1] == '-':
            num = int(lst[0]) - int(lst[2])
            if num == int(lst[-1]):
                answer += 'O'
            else:
                answer += 'X'
        else:
            num = int(lst[0]) + int(lst[2])
            if num == int(lst[-1]):
                answer += 'O'
            else:
                answer += 'X'
    return answer