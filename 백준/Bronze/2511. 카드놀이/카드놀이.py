# 백준 2511 카드놀이

import sys

A_num = list(map(int, sys.stdin.readline().split()))
B_num = list(map(int, sys.stdin.readline().split()))

A_score = 0
B_score = 0

for i in range(10):
    if A_num[i] > B_num[i]:
        A_score += 3
    elif A_num[i] < B_num[i]:
        B_score += 3
    else:
        A_score += 1
        B_score += 1
print(A_score, B_score)

if A_score == B_score:
    for i in range(9, -1, -1):
        if A_num[i] > B_num[i]:
            print('A')
            break
        elif A_num[i] < B_num[i]:
            print('B')
            break
    else:
        print('D')
else:
    if A_score > B_score:
        print('A')
    else:
        print('B')
