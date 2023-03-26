from itertools import product

def solution(word):
    char = ['A', 'E', 'I', 'O', 'U']
    lst = []
    
    for i in range(1, 6):
        for j in product(char, repeat=i):
            lst.append(''.join(j))

    lst.sort()
    answer = lst.index(word) + 1

    return answer