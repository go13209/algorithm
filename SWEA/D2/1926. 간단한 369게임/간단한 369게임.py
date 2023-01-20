N = int(input())

for n in range(1, N + 1):
    number = str(n)
    cnt = number.count('3') + number.count('6') + number.count('9')
    if cnt == 0:
        print(number, end=' ')
    else:
        print(cnt * '-', end=' ')