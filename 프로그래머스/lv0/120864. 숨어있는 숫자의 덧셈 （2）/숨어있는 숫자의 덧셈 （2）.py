def solution(my_string):
    answer = 0
    number = '0'
    for char in my_string:
        if char.isdecimal() == True:
            number += char
        else:
            answer += int(number)
            number = '0'
    else:
        answer += int(number)
    return answer