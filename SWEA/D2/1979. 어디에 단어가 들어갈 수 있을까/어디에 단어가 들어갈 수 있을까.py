T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    
    num_lst = []

    for n in range(N):
        num_lst.append(input().split())
    
    # 가로 구하기
    x_num_lst = num_lst
    x_cnt = 0

    for x_num in x_num_lst:
        x_n = ''.join(x_num)
        for x_str in x_n.split('0'):
            if x_str == '1'*K:
                x_cnt += 1
    
#     # 세로 구하기
    y_num_lst = [[] for _ in range(N)]
    y_cnt = 0
    for i in range(N):
        for j in range(N):
            y_num_lst[i].append(num_lst[j][i])

    for y_num in y_num_lst:
        y_n = ''.join(y_num)
        for y_str in y_n.split('0'):
            if y_str == '1' * K:
                y_cnt += 1

    print(f'#{t} {x_cnt + y_cnt}')