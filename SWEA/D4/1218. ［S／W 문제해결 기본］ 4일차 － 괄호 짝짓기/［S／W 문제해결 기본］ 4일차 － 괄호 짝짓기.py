for t in range(1, 11):
    N = int(input())
    str = input()
    dict = {
        '(' : 1, '[' : 2, '{' : 3, '<' : 4,
        ')' : -1, ']' : -2, '}' : -3, '>' : -4}
    total = 0
    for i in str:
        total += dict[i]
        if total < 0:
            print(f'#{t} 0')
            break
    else:
        if total == 0:
            print(f'#{t} 1')
        else:
            print(f'#{t} 0')