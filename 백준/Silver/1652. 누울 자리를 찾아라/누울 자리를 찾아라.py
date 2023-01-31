# 백준 1652 누울 자리를 찾아라
N = int(input())
matrix = [[char for char in input()] for _ in range(N)]
# 방의 크기 N을 입력받는다.
# 방의 구조를 나타내는 '.'와 'X' 문자열을 N만큼 입력받고 행렬의 형태로 저장한다.
# [['.', '.', '.', '.', 'X'],
#  ['.', '.', 'X', 'X', '.'],
#  ['.', '.', '.', '.', '.'],
#  ['.', 'X', 'X', '.', '.'],
#  ['X', '.', '.', '.', '.']]

# 1. 가로로 누울 자리 구하기
x_list = []
x_cnt = 0

for x in matrix:
    x = ''.join(x)
    x_list.append(x.split('X'))
# 새로운 리스트(x_list)를 만들어 행렬의 각 리스트 속 요소를 문자 'X'를 기준으로 쪼개어 저장한다.
# [['....', ''], ['..', '', '.'], ['.....'], ['.', '', '..'], ['', '....']]

for lst in x_list:
    for char in lst:
        if char.count('.') >= 2:
            x_cnt += 1
# x_list 속 요소를 순회하며 '.'이 2개 이상 붙어 있는 경우 누울 수 있는 자리 한 개로 카운트한다.

# 2. 세로로 누울 자리 구하기
y_matrix = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        y_matrix[i].append(matrix[j][i])
# 기존 행렬의 행 값을 열에, 열 값을 행에 넣어 열 우선 순회 매트릭스를 만든다.
# [['.', '.', '.', '.', 'X'],
#  ['.', '.', '.', 'X', '.'],
#  ['.', 'X', '.', 'X', '.'],
#  ['.', 'X', '.', '.', '.'],
#  ['X', '.', '.', '.', '.']]

y_cnt = 0
y_list = []

for y in y_matrix:
    y = ''.join(y)
    y_list.append(y.split('X'))
# 새로운 리스트(y_list)를 만들어 행렬의 각 리스트 속 요소를 문자 'X'를 기준으로 쪼개어 저장한다.
# [['....', ''], ['...', '.'], ['.', '.', '.'], ['.', '...'], ['', '....']]

for lst in y_list:
    for char in lst:
        if char.count('.') >= 2:
            y_cnt += 1
# y_list 속 요소를 순회하며 '.'이 2개 이상 붙어 있는 경우 누울 수 있는 자리 한 개로 카운트한다.

print(x_cnt, y_cnt)
# 5 4