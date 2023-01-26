T = int(input())

for t in range(T):
    string = input()
    PS = []
    
    for bracket in string:
        if bracket == '(':
            PS.append(bracket)
        elif bracket == ')':
            if len(PS) != 0:
                PS.pop()
            else:
                PS.append(bracket)
                break

    if len(PS) == 0:
        print('YES')
    else:
        print('NO')