input_list = list(map(int, input().split()))
number_list = []
for i in range(1, 9):
    number_list.append(i)
if number_list == input_list:
    print('ascending')
elif list(reversed(number_list)) == input_list:
    print('descending')
else:
    print('mixed')