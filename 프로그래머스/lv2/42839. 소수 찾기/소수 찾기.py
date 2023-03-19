from itertools import permutations

def solution(numbers):
    answer = 0
    
    num_set = set()
    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers, i):
            num = int(''.join(j))
            num_set.add(num)
    
    for num in num_set:
        if num < 2:
            continue
        else:
            for n in range(2, num):
                if num % n == 0:
                    break
            else:
                answer += 1

    return answer