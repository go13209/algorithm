N = int(input())
cnt = 0
if N%5 == 0:
    print(N//5)
else:
    while N >= 0:
        N -= 3
        cnt += 1
        if N % 5 == 0:
            print(N//5 + cnt)
            break
    else:
        print(-1)