def solution(board):
    dy = [-1, 1, 0, 0, -1, -1, 1, 1]
    dx = [0, 0, -1, 1, -1, 1, 1, -1]
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == 1:
                for i in range(8):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= nx < len(board) and 0 <= ny < len(board) and board[ny][nx] != 1:
                        board[ny][nx] = 2

    answer = 0
    for j in board:
        for k in j:
            if k == 0:
                answer += 1

    return answer