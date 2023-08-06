def solution(keyinput, board):
    w, h = board[0]//2, board[1]//2
    x, y = 0, 0
    for input in keyinput:
        if input == 'left':
            if x > -w:
                x -= 1
        elif input == 'right':
            if x < w:
                x += 1
        elif input == 'up':
            if y < h:
                y += 1
        else:
            if y > -h:
                y -= 1
        
    answer = [x, y]
    return answer