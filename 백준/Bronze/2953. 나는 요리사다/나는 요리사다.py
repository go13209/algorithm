scores = [list(map(int, input().split())) for _ in range(5)]
highest_score = sum(scores[-1])
number = 1
for score in scores:
    if sum(score) >= highest_score:
        highest_score = sum(score)
        number = 1 + scores.index(score)
print(number, highest_score)