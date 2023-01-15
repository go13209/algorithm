import sys

n = int(sys.stdin.readline())
number_list = list(map(int, sys.stdin.readline().split()))
sorted_list = sorted(number_list)
print(sorted_list[0], sorted_list[n-1])