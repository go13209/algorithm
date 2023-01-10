T = int(input())
for t in range(1, T + 1):
    numbers = list(map(int, (input().split())))
    cnt = len(numbers)
    total = sum(numbers)
    result = round(total / cnt)
    print(f'#{t} {round(total / cnt)}')