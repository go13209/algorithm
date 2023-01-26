# 백준 10773 제로
N = int(input())
# 테스트 케이스 수를 입력받는다.
numbers = []
# 번호를 저장할 빈 리스트 생성

for n in range(N):
    number = int(input())
    # 테스트 케이스 수만큼 for문을 돌려 번호를 입력받는다.
    if number != 0:
        numbers.append(number)
    else:
        numbers.pop()
    # 입력받은 번호가 0이 아닐 경우 리스트에 추가한다.
    # 입력받은 번호가 0일 경우 리스트에서 가장 최근에 추가된 값을 하나 삭제한다.

print(sum(numbers))
# 리스트에 저장된 숫자의 합을 출력