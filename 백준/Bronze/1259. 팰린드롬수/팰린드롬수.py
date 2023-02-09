# 백준 1259 팰린드롬수

while True:
    num = input()

    if num == '0':
        break

    reversed_num = ''

    for n in reversed(num):
        reversed_num += n

    if num == reversed_num:
        print('yes')
    else:
        print('no')