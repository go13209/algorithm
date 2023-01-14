import sys

input = sys.stdin.readline
T = int(input())
for t in range(T):
    numbers = list(map(int, input().split()))
    print(numbers[0] + numbers[1])