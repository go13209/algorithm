def solution(my_string):
    answer = ''
    vowel = ['a', 'e', 'i', 'o', 'u']
    for str in my_string:
        if str not in vowel:
            answer += str
    return answer