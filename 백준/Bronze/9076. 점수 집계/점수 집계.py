T = int(input())
numbers = []
for _ in range(T):
    numbers.append(sorted(list(map(int, input().split()))))

for num in numbers:
    if abs(num[1] - num[3]) >= 4:
        print('KIN')
    else:
        print(sum(num[1:4]))