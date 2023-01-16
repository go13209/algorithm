T = int(input())
for t in range(1, T + 1):
    score = 0
    score_list = []
    input_o_x = list(map(str, input()))
    for o_x in input_o_x:
        if o_x == 'O':
            score += 1
            score_list.append(score)
        else:
            score = 0
    print(sum(score_list))