# 백준 7568 덩치
import sys
input = sys.stdin.readline

N = int(input())
# 전체 사람의 수를 입력받는다.

lst = []

for _ in range(N):
    weight, height = map(int, input().split())
    lst.append((weight, height))
# 사람들의 키와 몸무게를 (몸무게, 키) 형식의 튜플로 리스트에 저장한다.

rank = []
# 등수를 저장할 리스트를 만든다.

for i in range(N):
    cnt = 0
    for j in range(N):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            cnt += 1
    rank.append(cnt + 1)
# 등수는 자신보다 키와 몸무게 모두 큰 사람의 수 + 1 이다.
# 각 사람들의 등수를 리스트에 저장한다.

for r in rank:
    print(r, end=' ')
# 등수를 출력한다.