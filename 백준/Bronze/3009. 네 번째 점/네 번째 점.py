x_list = []
y_list = []
for t in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
if sorted(x_list)[0] == sorted(x_list)[1]:
    new_x = sorted(x_list)[2]
else:
    new_x = sorted(x_list)[0]
if sorted(y_list)[0] == sorted(y_list)[1]:
    new_y = sorted(y_list)[2]
else:
    new_y = sorted(y_list)[0]
print(new_x, new_y)