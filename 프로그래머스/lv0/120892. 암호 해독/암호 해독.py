def solution(cipher, code):
    answer = ''
    for n in range(1, len(cipher)//code + 1):
        answer += cipher[n*code - 1] 
    return answer