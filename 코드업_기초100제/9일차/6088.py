# 코드업 파이썬 기초 100제
# 6088

a, d, n = map(int, input().split())
cnt = 1
while True:
    if cnt == n:
        print(a)
        break
    a += d
    cnt += 1