def solution(emergency):
    answer = []
    dict = {}
    for num in range(1, len(emergency)+1):
        dict[sorted(emergency, reverse=True)[num-1]] = num
    for e in emergency:
        answer.append(dict[e]) 
    return answer