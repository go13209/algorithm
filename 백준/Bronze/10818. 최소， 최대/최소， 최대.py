T = int(input())
numbers = sorted(list(map(int, input().split())))
print(f'{numbers[0]} {numbers[T - 1]}')