def solution(n):
    answer = 0
    total = 1
    num = 1
    while n >= total:
        total *= num
        num += 1
        answer += 1
    
    return answer - 1