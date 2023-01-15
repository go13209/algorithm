list = []
cnt = 0
for n in range(1, 11):
    number = int(input())
    remainder = number % 42
    if remainder not in list:
        list.append(remainder)
        cnt += 1
print(cnt)