n = int(input())
nums = sorted(list(map(int, input().split())))
total = 0
time = 0
for i in nums:
    time += i
    total += time
print(total)