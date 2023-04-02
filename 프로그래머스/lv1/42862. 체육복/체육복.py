def solution(n, lost, reserve):
    lst = [0]

    for i in range(1, n + 1):
        lst.append(1)
        if i in lost:
            lst[i] -= 1
        if i in reserve:
            lst[i] += 1
    lst.append(0)


    for j in range(1, n + 1):
        if lst[j] == 0: 
            if lst[j - 1] == 2:
                lst[j] += 1
                lst[j - 1] -= 1
                continue
                
            elif lst[j + 1] == 2:
                lst[j] += 1
                lst[j + 1] -= 1
                continue
    
    answer = 0
    for k in lst:
        if k >= 1:
            answer += 1

    return answer