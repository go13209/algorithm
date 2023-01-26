def solution(age):
    answer = ''
    dict = {}
    n = 0
    for i in range(ord('a'), ord('j')+1):
        dict[n] = chr(i)
        n += 1
    for a in str(age):
        answer += dict[int(a)]
    return answer