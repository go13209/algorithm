a, b = map(int, input().split())
word = []
cnt = 0

for _ in range(a):
    word.append(input())
for _ in range(b):
    str = input()
    if str in word:
        cnt += 1
print(cnt)