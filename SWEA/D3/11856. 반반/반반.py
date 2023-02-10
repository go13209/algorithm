# SWEA 11856 반반

T = int(input())
# 테스트 케이스 수를 입력받는다.

for t in range(1, T + 1):
    word = input()
    # 문자열을 입력받는다.

    for i in word:
        if word.count(i) != 2:
            print(f'#{t} {"No"}')
            break

    else:
        print(f'#{t} {"Yes"}')
    # 문자열의 길이는 4이고 2개의 서로 다른 문자가 두 번씩 등장해야 한다.
    # 따라서 문자열의 한 글자씩 불러와 확인했을 때 문자열 속 해당 알파벳의 개수가 정확히 2개씩이어야 한다.
    # 'ABAB'를 예로 들면 'A'와 'B'가 각각 2개여야 한다.
    # 2개 아닐 경우 반복문을 종료하고 'No'를 출력한다.
    # 문제 없이 반복문이 종료되었을 경우 'Yes'를 출력한다.
