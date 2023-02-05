numbers = []

for _ in range(9):
    numbers.append(list(map(int, input().split())))

max_value = 0
x = 0 ; y = 0

for i in range(9):
    for j in range(9):
        if numbers[i][j] >= max_value:
            max_value = numbers[i][j]
            x = i + 1
            y = j + 1
print(max_value)
print(x, y)