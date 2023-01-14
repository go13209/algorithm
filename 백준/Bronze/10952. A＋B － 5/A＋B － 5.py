import sys

while True:
    numbers = list(map(int, sys.stdin.readline().split()))
    if numbers[0] + numbers[1] > 0:
        print(numbers[0] + numbers[1])
    else:
        break