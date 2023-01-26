def solution(my_string):
    answer = []
    for str in my_string:
        if str.isdecimal() == True:
            answer.append(int(str))
    return sorted(answer)