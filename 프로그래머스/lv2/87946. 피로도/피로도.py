from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for case in permutations(dungeons, len(dungeons)):
        cnt = 0
        energy = k

        for minimum, cost in case:
            if energy >= minimum:
                cnt += 1
                energy -= cost

        if cnt > answer:
            answer = cnt
    
    return answer