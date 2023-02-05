N, M = map(int, input().split())
numbers = []
total = [[] for _ in range(N)]

for _ in range(N * 2):
    numbers.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        total[i].append(numbers[i][j] + numbers[i + N][j])

for t in total:
    for c in t:
        print(c, end=' ')
    print()