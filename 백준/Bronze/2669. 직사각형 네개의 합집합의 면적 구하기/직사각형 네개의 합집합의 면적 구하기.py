x_y = set()

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            x_y.add((i, j))
print(len(x_y))