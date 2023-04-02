def solution(name):
    answer = 0
    
    for char in name:
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

    min_move = len(name) - 1
    for i in range(len(name)):
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        min_move = min(min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next))

    answer += min_move
    
    return answer