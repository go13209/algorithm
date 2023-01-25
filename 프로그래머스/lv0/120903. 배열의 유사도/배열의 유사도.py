def solution(s1, s2):
    answer = 0
    for s_1 in s1:
        if s_1 in s2:
            answer += 1
    return answer