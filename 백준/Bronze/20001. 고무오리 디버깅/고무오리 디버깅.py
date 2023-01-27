start = input()
list = []

while True:
    str = input()
    if str == '고무오리 디버깅 끝':
        break
    elif str == '문제':
        list.append(str)
    else:
        if list:
            list.pop()
        else:
            list.append('문제')
            list.append('문제')

if list:
    print('힝구')
else:
    print('고무오리야 사랑해')