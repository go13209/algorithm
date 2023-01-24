T = int(input())

for t in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    max_value = numbers[-1]
    total = 0

    for n in range(N - 2, -1, -1):
        if max_value <= numbers[n]:
            max_value = numbers[n]
        else:
            total += max_value - numbers[n]
    print(f'#{t} {total}')