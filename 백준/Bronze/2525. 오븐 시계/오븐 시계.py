current_time = list(map(int, input().split()))
cooking_time = int(input())
hour = current_time[0]
minutes = current_time[1] + cooking_time

if minutes >= 60: # 120
    hour = current_time[0] + (minutes // 60)
    minutes = minutes % 60 
    if hour >= 24:
        hour -= 24
print(hour, minutes)