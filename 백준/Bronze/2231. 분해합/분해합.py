N = int(input())

for i in range(1, N + 1):
    number_list = list(map(int, str(i)))
    total = i + sum(number_list)
    if total == N:
        print(i)
        break
    elif i == N:
        print(0)