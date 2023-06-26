# 코드업 파이썬 기초 100제
# 6089

a, r, n = map(int, input().split())
cnt = 1
while True:
    if cnt == n:
        print(a)
        break
    a *= r
    cnt += 1