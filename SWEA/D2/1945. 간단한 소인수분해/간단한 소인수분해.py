# SWEA 1945 간단한 소인수분해

T = int(input())
# 테스트 케이스 수를 입력받는다.

for t in range(1, T + 1):

    divisor = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}
    # 딕셔너리를 만들고 2, 3, 5, 7, 9, 11을 key로 소인수의 개수를 value로 설정한다.

    N = int(input())
    # 숫자 N을 입력받는다.

    while N > 1:
        for k in divisor.keys():
            if N % k == 0:
                divisor[k] += 1
                N = N // k
                if N == 1:
                    break
    # 숫자 N을 딕셔너리 안의 key로 나누고 나누어떨어지면 해당 value에 1을 더한다.
    # 위 과정을 N이 1이 될 때까지 반복한다.

    value_lst = [v for v in divisor.values()]
    # 딕셔너리의 value 리스트를 만든다.

    print(f'#{t}', *value_lst)
    # 숫자 N의 소인수(2, 3, 5, 7, 9, 11) 각각의 개수를 출력한다.
