n = int(input())
for _ in range(n):
    case = list(map(int, input().split()))
    cnt = 0
    average = sum(case[1:]) / case[0]
    for score in case[1:]:
        if score > average:
            cnt += 1
    print(format(cnt/case[0]*100, '.3f')+'%')   