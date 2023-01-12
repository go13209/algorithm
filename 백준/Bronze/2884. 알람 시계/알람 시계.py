n = list(map(int, input().split()))

total = (n[0] * 60) + n[1]
early_hour = (total - 45) // 60
early_minute = (total - 45) % 60
if early_hour < 0:
    early_hour += 24
print(early_hour, early_minute)