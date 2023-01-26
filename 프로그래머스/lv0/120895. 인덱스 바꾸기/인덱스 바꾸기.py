def solution(my_string, num1, num2):
    answer = ''
    list = [str for str in my_string]
    list[num1], list[num2] = list[num2], list[num1]
    for i in list:
        answer += i
    return answer