w_score = []
k_score = []

for i in range(20):
    if i < 10:
        w_score.append(int(input()))
    else:
        k_score.append(int(input()))
w_score.sort(reverse=True)
k_score.sort(reverse=True)

print(sum(w_score[0:3]), sum(k_score[0:3]))