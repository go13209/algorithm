import sys
input = sys.stdin.readline

numbers = []

N = int(input())
for _ in range(N):
    numbers.append(int(input()))

last = numbers[-1]
cnt = 1

for num in numbers[::-1]:
    if num > last:
        last = num
        cnt += 1

print(cnt)