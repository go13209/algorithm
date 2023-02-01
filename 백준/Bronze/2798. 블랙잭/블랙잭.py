N, M = map(int, input().split())
numbers = list(map(int, input().split()))
total = 0

for x in range(N-2):
    for y in range(x+1, N-1):
        for z in range(y+1, N):
            if total < numbers[x] + numbers[y] + numbers[z] <= M:
                total = numbers[x] + numbers[y] + numbers[z]
print(total)