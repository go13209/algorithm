scores = [list(map(int, input().split())) for _ in range(5)]
# 요리사 다섯 명의 점수를 이중리스트의 형태로 입력받는다.
highest_score = sum(scores[0])
number = 1
# 가장 높은 점수를 첫 번째 요리사의 점수로 임의 설정해놓는다.
for score in scores:
    if sum(score) > highest_score:
        highest_score = sum(score)
        number = 1 + scores.index(score)
# for문을 돌려 첫 번째 요리사의 점수보다 높은 점수가 있을 경우 새롭게 highest_score 변수에 저장한다.
# 오리사의 번호는 0이 아닌 1부터이므로 1을 더한다. 
print(number, highest_score)
# 우승자의 번호와 점수를 출력한다.