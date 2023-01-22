N = int(input())
# 테스트 케이스 수 입력받기
group_word = 0
# 맨 처음 그룹 단어의 개수 0으로 설정하기
for n in range(1, N + 1):
    word = input()
    x = 0
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            if word[i] in word[i+1:]:
                x += 1
    # 입력한 글자수의 -1만큼 for 문을 돌리는데 if 조건절에 'i+1'이 있기 때문에 range 범위를 그냥 단어의 철자수로 설정할 경우 오류 발생
    # 단어의 첫 글자와 그 다음 글자가 다를 경우 첫 글자가 단어의 나머지 부분에 또 있는지 확인한다.
    # 첫 글자가 연속되지 않았음에도 다른 곳에 또 있을 경우 그룹 단어가 아니므로 잘못되었단 의미의 x 변수에 1을 더한다.
    # x 값이 0일 경우 해당 단어에 문제가 없다는 의미이므로 그룹 단어로 하나 카운트한다.
    if x == 0:
        group_word += 1
print(group_word)