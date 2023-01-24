T = int(input())

for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    new_numbers = []
    for number in numbers:
        if number != max(numbers):
            if number != min(numbers):
                new_numbers.append(number)
    print(f'#{t} {round(sum(new_numbers) / len(new_numbers))}')