from itertools import combinations

def solution(nums):
    answer = 0
    num_lst = list(combinations(nums, 3))
    for lst in num_lst:
        for i in range(2, sum(lst)):
            if sum(lst) % i == 0:
                break
        else:
            answer += 1
    return answer