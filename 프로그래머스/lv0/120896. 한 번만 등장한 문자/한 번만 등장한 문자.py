def solution(s):
    answer = ''
    for char in sorted(s):
        if sorted(s).count(char) == 1:
            answer += char
    return answer