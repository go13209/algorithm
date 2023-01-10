T = int(input())
for t in range(1, T + 1):
    numbers = list(map(int, input().split()))
    result = 0
    for n in numbers:
        if n > result:
            result = n
    print(f'#{t} {result}')