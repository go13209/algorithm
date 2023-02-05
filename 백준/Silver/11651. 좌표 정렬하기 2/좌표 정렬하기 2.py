import sys

N = int(sys.stdin.readline())
# 점의 개수 N을 입력받는다.

numbers = []
# 좌표를 저장할 빈 리스트를 만든다.

for _ in range(N):
    numbers.append(tuple(map(int, sys.stdin.readline().split())))
# N번만큼 좌표를 입력받는다.

sorted_numbers = sorted(numbers, key = lambda x: (x[1], x[0]))
# 좌표를 저장한 리스트를 x 좌표 1순위, y 좌표를 2순위로 오름차순 정렬한다.

for x, y in sorted_numbers:
    print(x, y)
# 정렬한 리스트의 x, y 좌표를 차례로 출력한다.