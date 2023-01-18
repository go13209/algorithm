croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
str = input()
cnt = 0
for char in croatia:
    if char in str:
        cnt += str.count(char)
print(cnt + (len(str) - (cnt * 2)))