# SWEA 1959 두 개의 숫자열

T = int(input())
# 테스트 케이스 수를 입력받는다.

for t in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # N개의 숫자로 구성된 숫자열 A와 M개의 숫자로 구성된 숫자열 B를 입력받는다.

    lst = []
    # 마주 보는 숫자들을 곱한 수를 모두 더한 값을 리스트에 저장하여 비교할 수 있도록 빈 리스트를 만든다.

    for i in range(abs(N - M) + 1):
        # 더 긴 쪽의 양 끝을 벗어나지 않으면서 서로 마주 볼 수 있는 경우의 수는 N - M + 1이다.
        # 예를 들어 N이 3, M이 5라면 서로 마주 볼 수 있는 경우의 수는 3가지이다.
        # 음수가 나오는 때를 대비해 절댓값으로 만든다.

        total = 0
        # 마주 보는 숫자들을 곱한 수를 더해나갈 변수를 만들고 0을 저장한다.

        if N < M:
            for j in range(N):
                total += A[j] * B[j + i]

            lst.append(total)

        else:
            for k in range(M):
                total += A[k + i] * B[k]

            lst.append(total)
        # A의 숫자와 마주 보는 B의 숫자를 곱해 total 변수에 더하고 최종값을 리스트에 저장한다.

    print(f'#{t} {max(lst)}')
    # 리스트에 저장된 값 중 최댓값을 출력한다.
