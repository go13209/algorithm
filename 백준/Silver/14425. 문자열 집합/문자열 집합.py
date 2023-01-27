a, b = map(int, input().split())
A = set()
cnt = 0

for _ in range(a):
    A.add(input())
for _ in range(b):
    word = input()
    if word in A:
        cnt += 1

print(cnt)