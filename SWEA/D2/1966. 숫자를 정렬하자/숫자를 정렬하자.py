# SWEA 1966 숫자를 정렬하자

T = int(input())
# 테스트 케이스 수를 입력받는다.

for t in range(1, T + 1):
    N = int(input())
    # 수의 개수 N을 입력받는다.

    nums = list(map(int, input().split()))
    # 숫자들을 입력받아 리스트로 만든다.

    print(f'#{t}', *sorted(nums))
    # 리스트를 오름차순으로 정렬하여 출력한다.
