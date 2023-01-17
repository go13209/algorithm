number_list = input().split()
number1 = ''
number2 = ''
for i in range(4):
    if i < 2:
        number1 += number_list[i]
    else:
        number2 += number_list[i]
print(int(number1) + int(number2))