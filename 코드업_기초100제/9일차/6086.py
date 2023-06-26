# 코드업 파이썬 기초 100제
# 6086

n = int(input())
total = 0
start = 1
while True:
    total += start
    start += 1
    if total >= n:
        break
print(total)