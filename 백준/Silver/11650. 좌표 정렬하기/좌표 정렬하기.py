N = int(input())
numbers = []

for _ in range(N):
    numbers.append(tuple(map(int, input().split())))

sorted_numbers = sorted(numbers, key = lambda x: (x[0], x[1]))

for x, y in sorted_numbers:
    print(x, y)