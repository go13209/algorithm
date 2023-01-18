croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
str = input()
cnt = 0
for char in croatia:
    if char in str:
        str = str.replace(char, '!')
print(len(str))