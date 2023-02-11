# SWEA 1940 가랏! RC카!

T = int(input())
# 테스트 케이스 수를 입력받는다.

for t in range(1, T + 1):
    N = int(input())
    # 명령의 개수를 입력받는다.

    m = 0
    current_speed = 0
    # 이동 거리와 현재 속도를 저장할 변수를 만들고 0으로 설정한다.

    for n in range(1, N + 1):
        speed = list(map(int, input().split()))
        # 가속(1) 또는 감속(2), 값을 입력받아 리스트로 만든다.

        if speed[0] == 1:
            current_speed += speed[1]
            m += current_speed
        # 리스트의 첫 번째 요소가 1이면 가속을 의미한다.
        # 현재 속도에 리스트의 첫 번째 값을 더하고 이동 거리에 현재 속도 값을 더한다.

        elif speed[0] == 2:
            if current_speed < speed[1]:
                speed[1] = 0
            current_speed -= speed[1]
            m += current_speed
        # 리스트의 첫 번째 요소가 2이면 감속을 의미한다.
        # 현재 속도에서 리스트의 첫 번째 값만큼 감하고 이동 거리에 현재 속도 값을 더한다.
        # 단, 현재 속도보다 감속할 속도가 더 클 경우 속도를 0으로 한다.

        else:
            m += current_speed
        # 리스트에 첫 번째 요소가 0이라면 현재 속도를 유지하라는 의미이다.
        # 이동 거리에 현재 속도 값을 더한다.

    print(f'#{t} {m}')
    # 최종 이동 거리를 출력한다.
