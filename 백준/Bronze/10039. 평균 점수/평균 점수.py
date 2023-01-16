score_list = []
new_score_list = []
for n in range(5):
    score = int(input())
    score_list.append(score)
for each_score in score_list:
    if each_score < 40:
        each_score = 40
        new_score_list.append(each_score)
    else:
        new_score_list.append(each_score)
print(int(sum(new_score_list) / 5))