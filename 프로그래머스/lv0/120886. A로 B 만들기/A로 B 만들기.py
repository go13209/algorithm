def solution(before, after):
    answer = 0
    cnt = 0
    for char in before:
        if before.count(char) == after.count(char):
            cnt += 1
    if cnt == len(after):
        answer = 1
    else:
        answer = 0
    return answer