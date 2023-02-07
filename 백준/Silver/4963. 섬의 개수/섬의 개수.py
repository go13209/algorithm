# 백준 4963 섬의 개수
import sys

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]
# 8방향 순회를 위해 행과 열 리스트를 만든다.

while True:
    width, height = map(int, sys.stdin.readline().split())
    # 지도의 너비와 높이를 입력받는다.

    if width == 0 and height == 0:
        break
    # 입력에 0이 두 개 주어지면 반복문을 종료한다.

    graph = []
    
    for _ in range(height):
        graph.append(list(map(int, sys.stdin.readline().split())))
    # 지도를 이차원 리스트로 저장한다.
    
    cnt = 0
    # 섬의 개수를 세는 변수를 만든다.

    for h in range(height):
        for w in range(width):
            if graph[h][w] == 1:
                stack = [(h, w)]
                graph[h][w] = 0
                cnt += 1
    # 지도의 정사각형을 하나씩 순회한다.
    # 정사각형이 1(땅)일 경우 해당 영역을 0(바다)으로 바꾸고 카운트에 1을 더한다.

                while stack:
                    x, y  = stack.pop()
                    for i in range(8):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < height and 0 <= ny < width and graph[nx][ny] == 1:
                            stack.append((nx, ny))
                            graph[nx][ny] = 0
                # 1(땅)이었던 영역과 연결된 땅이 있는지 확인하기 위해 8방향 델타값을 순회한다.
                # 지도를 벗어나지 않는 8방향 영역 중 1(땅)이 있으면 해당 영역을 새로운 기준으로 삼고 0으로 바꾼다.
                # 이 과정을 연결된 땅이 더 이상 없을 때까지 반복한다.

    print(cnt)
    # 카운트된 섬의 개수를 출력한다.