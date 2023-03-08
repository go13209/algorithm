def solution(array, commands):
    answer = []
    
    for n in range(len(commands)):
        i, j, k = commands[n]
        lst = array[i-1:j]
        lst.sort()
        answer.append(lst[k-1])
    
    return answer