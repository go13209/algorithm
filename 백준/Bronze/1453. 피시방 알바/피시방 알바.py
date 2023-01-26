N = int(input())
seat_list = []
cnt = 0
customers = map(int, input().split())
for customer in customers:
    if customer not in seat_list:
        seat_list.append(customer)
    else:
        cnt += 1
print(cnt)
