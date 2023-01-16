number_of_questions = int(input())
answers = list(map(int, input().split()))
score = 0
score_list = []
for answer in answers:
    if answer == 1:
        score += 1
        score_list.append(score)
    else:
        score = 0
print(sum(score_list))