import sys

a, b = map(int, sys.stdin.readline().split())
number_list = list(map(int, sys.stdin.readline().split()))
new_list = []
for number in number_list:
    if number < b:
        new_list.append(number)
for n in new_list:
    print(n, end=' ')