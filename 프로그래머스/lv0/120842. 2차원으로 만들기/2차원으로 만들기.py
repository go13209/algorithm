def solution(num_list, n):
    answer = [[]]
    i = 0
    for num in num_list:
        answer[i].append(num)
        if len(answer[i]) == n:
            answer.append([])
            i += 1
    if [] in answer:
        answer.remove([])
    return answer