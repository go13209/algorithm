T = int(input())

for i in range(1, T + 1):
    students, o_task = map(int, input().split())
    submit = list(map(int, input().split()))
    x_task = ''

    for n in range(1, students + 1):
        if n not in submit:
            x_task += str(n) + ' '
    print(f'#{i} {x_task}')