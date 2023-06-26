# 코드업 파이썬 기초 100제
# 6090

a, m, d, n = map(int, input().split())
cnt = 1
while True:
    if cnt == n:
        print(a)
        break
    a = a * m + d
    cnt += 1