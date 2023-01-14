N = int(input())
numbers = list(map(int, input().split()))
finding_number = int(input())
cnt = 0
for n in numbers:
    if finding_number == n:
        cnt += 1
print(cnt)
