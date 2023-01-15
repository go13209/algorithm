N = int(input())
scores = list(map(int, input().split()))
new_scores = []
for score in scores:
    new_score = score / max(scores) * 100
    new_scores.append(new_score)
print(sum(new_scores) / N)