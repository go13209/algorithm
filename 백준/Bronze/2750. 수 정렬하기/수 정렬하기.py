T = int(input())
list = []
for t in range(T):
    number = int(input())
    list.append(number)
for i in sorted(list):
    print(i)