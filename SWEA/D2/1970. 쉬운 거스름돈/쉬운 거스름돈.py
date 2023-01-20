T = int(input())

for t in range(1, T + 1):
    money = int(input())
    money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    rest = []
    for i in money_list:
        rest.append(money // i)
        money -= i * (money//i)
    print(f'#{t}')
    print(*rest)