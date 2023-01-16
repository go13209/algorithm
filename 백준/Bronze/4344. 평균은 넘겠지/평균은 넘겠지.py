T = int(input())
for t in range(T):
    number_line = list(map(int, input().split()))
    students = number_line[0]
    scores = number_line[1:]
    cnt = 0
    for score in scores:
        if score > (sum(scores) / students):
            cnt += 1
    print('{:0.3f}'.format(round(cnt/students*100, 3)) + '%')