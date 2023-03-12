import sys
from collections import Counter

N = int(sys.stdin.readline())
card_nums = Counter(list(map(int, sys.stdin.readline().split())))

M = int(sys.stdin.readline())
finding_nums = list(map(int, sys.stdin.readline().split()))


for i in finding_nums:
    print(card_nums[i], end=' ')