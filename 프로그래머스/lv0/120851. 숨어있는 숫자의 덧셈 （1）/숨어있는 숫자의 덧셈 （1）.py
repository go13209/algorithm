def solution(my_string):
    answer = 0
    for n in range(1, 10):
        if str(n) in my_string:
            answer += n * my_string.count(str(n))
    return answer