import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
new_array = sorted(set(numbers))
dict = {new_array[i]: i for i in range(len(new_array))}

for num in numbers:
    print(dict[num], end=' ')