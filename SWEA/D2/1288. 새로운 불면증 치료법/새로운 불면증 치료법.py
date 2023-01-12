T = int(input())
for t in range(1, T + 1):
    number =  int(input())
    s = set()
    cnt = 1
    while True:
        for n in list(str(number)):
            s.add(n)
        if len(s) == 10:
            break
        number //= cnt
        cnt += 1
        number *= cnt
    print(f'#{t} {number}')