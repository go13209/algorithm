# 코드업 파이썬 기초 100제
# 6082

n = int(input())
for i in range(1, n+1):
    if i % 10 in [3, 6, 9]:
        print('X', end=' ')
    else:
        print(i, end=' ')