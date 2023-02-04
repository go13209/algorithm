T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    numbers = []

    for _ in range(N):
        numbers.append(list(map(int, input().split())))
    
    max_total = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for r in range(M):
                for c in range(M):
                    total += numbers[i + r][j + c]
            if total > max_total:
                max_total = total
    print(f'#{t} {max_total}')