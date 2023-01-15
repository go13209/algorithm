o_list = []
x_list = []
for n in range(1, 29):
    number = int(input())
    o_list.append(number)

for i in range(1, 31):
    if i not in o_list:
        x_list.append(i)

print(*x_list, sep='\n')