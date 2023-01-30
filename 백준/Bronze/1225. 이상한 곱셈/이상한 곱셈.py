import sys

numbers = [list(num) for num in sys.stdin.readline().split()]

print(sum(map(int, numbers[0])) * sum(map(int, numbers[1])))