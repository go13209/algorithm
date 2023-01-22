# 백준 1065 한수
N = int(input())
cnt = 0
for n in range(1, N + 1):
    if n > 99:
        if int(str(n)[1]) - int(str(n)[0]) == int(str(n)[2]) - int(str(n)[1]):
            cnt += 1
    else:
        cnt += 1
print(cnt)