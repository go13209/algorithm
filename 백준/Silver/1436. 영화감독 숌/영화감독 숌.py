N = int(input())
lst = []
i = 666
while True:
    if '666' in str(i):
        lst.append(i)
        if lst.index(i) == N-1:
            print(i)
            break
    i += 1