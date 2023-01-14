import sys

input = sys.stdin.readline
T = int(input())
for t in range(1, T + 1):
    numbers = list(map(int, input().split()))
    print(f'Case #{t}: {numbers[0] + numbers[1]}')