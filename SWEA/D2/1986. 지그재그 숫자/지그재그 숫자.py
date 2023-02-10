# SWEA 1986 지그재그 숫자

T = int(input())
# 테스트 케이스 수를 입력받는다.

for t in range(1, T + 1):
    N = int(input())
    total = 0
    # 숫자 N을 입력받고 최종값을 구하기 위해 total 변수를 만들고 0을 저장한다.

    for n in range(1, N + 1):
        if n % 2 == 0:
            total -= n
        else:
            total += n
    # 1부터 N까지의 숫자를 하나씩 불러와 홀수이면 더하고 짝수이면 뺀다.

    print(f'#{t} {total}')
    # 최종값을 출력한다.
