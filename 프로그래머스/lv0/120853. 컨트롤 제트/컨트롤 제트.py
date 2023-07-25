def solution(s):
    lst = list(s.split())
    answer = 0
    num = 0
    for i in lst:
        if i == ' ':
            pass
        elif i == 'Z':
            answer -= num
        else:
            answer += int(i)
            num = int(i)
    return answer