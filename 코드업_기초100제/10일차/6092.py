# 코드업 파이썬 기초 100제
# 6092

lst = [0 for _ in range(24)]
n = int(input())
nums = list(map(int, input().split()))
for i in range(n):
    lst[nums[i]] += 1
print(*lst[1:])