total = 0
nums = [int(input()) for _ in range(10)]

for num in nums:
    total += num
    if total == 100:
        break
    elif total > 100:
        if abs(total - 100) <= abs((total - num) - 100):
            break
        else:
            total -= num
            break
print(total)