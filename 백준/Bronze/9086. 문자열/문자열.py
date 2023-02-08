# 백준 9086 문자열

T = int(input())
# 테스트 케이스 수를 입력받는다.

for _ in range(T):
    word = input()
    print(word[0] + word[-1])
# 입력받은 문자열의 첫 글자와 마지막 글자를 더해 하나의 문자열로 출력한다.
