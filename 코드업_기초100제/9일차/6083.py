# 코드업 파이썬 기초 100제
# 6083

r, g, b = map(int, input().split())
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
print(r*g*b)