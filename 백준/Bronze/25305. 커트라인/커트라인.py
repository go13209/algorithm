student, prize = map(int, input().split())
score = list(map(int, input().split()))
score.sort(reverse=True)
print(score[prize-1])