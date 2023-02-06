import sys

str  = sys.stdin.readline()

happy_cnt = 0 ; sad_cnt = 0

for i in range(len(str)):
    if str[i] == ':':
        if str[i:i+3] ==':-)':
            happy_cnt += 1
        if str[i:i+3] == ':-(':
            sad_cnt += 1

if sad_cnt < happy_cnt:
    print('happy')
elif sad_cnt > happy_cnt:
    print('sad')
elif sad_cnt == happy_cnt:
    if sad_cnt >= 1:
        print('unsure')
    else:
        print('none')