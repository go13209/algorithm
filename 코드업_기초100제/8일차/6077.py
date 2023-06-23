# 코드업 파이썬 기초 100제
# 6077

total = 0
n = int(input())
for i in range(1, n + 1):
    if i % 2 == 0:
        total += i
print(total)