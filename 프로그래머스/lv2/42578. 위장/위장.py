def solution(clothes):
    answer = 1
    dict = {}
    for cloth in clothes:
        if cloth[1] not in dict:
            dict[cloth[1]] = [cloth[0]]
        else:
            dict[cloth[1]] += [cloth[0]]
    
    for key in dict.keys():
        answer *= len(dict[key]) + 1
    return answer - 1