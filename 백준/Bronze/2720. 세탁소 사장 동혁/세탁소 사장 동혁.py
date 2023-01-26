T = int(input())
units = [25, 10, 5, 1]
for t in range(T):
    money = int(input())
    for unit in units:
        print(money//unit, end=' ')
        money -= unit * (money//unit)