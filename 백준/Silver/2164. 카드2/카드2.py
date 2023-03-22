# 백준 2164 카드2

import sys
from collections import deque

nums = deque([i for i in range(1, int(sys.stdin.readline()) + 1)])

for _ in range(len(nums)):
    if len(nums) == 1:
        print(nums[0])
        break
    else:
        nums.popleft()
        nums.append(nums.popleft())
