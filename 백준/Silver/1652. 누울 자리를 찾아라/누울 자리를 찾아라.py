# 백준 1652 누울 자리를 찾아라
N = int(input())
matrix = [[char for char in input()] for _ in range(N)]

# 1. 가로로 누울 자리 구하기
x_matrix = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        x_matrix[i].append(matrix[i][j])

x_list = []
x_cnt = 0

for x in x_matrix:
    x = ''.join(x)
    x_list.append(x.split('X'))

for lst in x_list:
    for char in lst:
        if char.count('.') >= 2:
            x_cnt += 1

# 2. 세로로 누울 자리 구하기
y_matrix = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        y_matrix[i].append(matrix[j][i])

y_cnt = 0
y_list = []

for y in y_matrix:
    y = ''.join(y)
    y_list.append(y.split('X'))

for lst in y_list:
    for char in lst:
        if char.count('.') >= 2:
            y_cnt += 1

print(x_cnt, y_cnt)