def solution(array):
    lst = [0 for _ in range(max(array) + 1)]
    for i in array:
        lst[i] += 1
    
    sorted_lst = sorted(lst, reverse=True)
    
    if sorted_lst[0] == sorted_lst[1]:
        return -1
    else:
        return lst.index(max(lst))