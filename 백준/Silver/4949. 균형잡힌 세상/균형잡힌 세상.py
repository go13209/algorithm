while True:
    str = input()
    lst = [[]]
    if str == '.':
        break
    
    for s in str:
        if s == '(' or s == '[':
            lst.append(s)
        elif s == ')':
            if lst[-1] == '(':
                lst.pop()
            else:
                lst.append(')')
                break
        elif s == ']':
            if lst[-1] == '[':
                lst.pop()
            else:
                lst.append(']')
                break
    if len(lst) == 1:
        print('yes')
    else:
        print('no')