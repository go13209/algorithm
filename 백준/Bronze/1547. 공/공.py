cups = [[], [1], [0], [0]]
N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    cups[x], cups[y] = cups[y], cups[x]

for i in range(len(cups)):
    if 1 in cups[i]:
        print(i)