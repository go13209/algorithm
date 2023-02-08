# 백준 10872 팩토리얼

N = int(input())
# 정수를 입력받는다.

total = 1
# 결괏값을 구하기 위해 total 변수를 만들고 1을 저장한다.

if N == 0:
    print(1)
# N이 0일 경우 1을 출력한다.

else:
    for n in range(1, N + 1):
        total *= n
    print(total)
# N이 0 이외의 수일 경우 1부터 해당 수까지 곱한 값을 출력한다.