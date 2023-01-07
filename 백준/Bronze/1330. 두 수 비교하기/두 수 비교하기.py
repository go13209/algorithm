number = list(map(int, input().split()))

if number[0] > number[1]:
    print('>')
elif number[0] < number[1]:
    print('<')
elif number[0] == number[1]:
    print('==')