def solution(spell, dic):
    for word in dic:
        cnt = 0
        for char in spell:
            if char in word:
                cnt += 1
        if cnt == len(spell):
            return 1
        
    return 2