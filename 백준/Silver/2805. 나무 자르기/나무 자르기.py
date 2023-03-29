# 백준 2805 나무 자르기

N, M = map(int, input().split())
# 나무의 수 N과 상근이가 가져갈 나무의 길이 M을 입력받는다.

trees = list(map(int, input().split()))
# 나무의 길이를 입력받는다.

start = 1
end = max(trees)
# 가장 짧은 길이 1을 start로, 가장 긴 나무 길이를 end로 설정한다.

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    # start와 end의 중간값을 mid로 설정한다.

    for tree in trees:
        if tree > mid:
            cnt += tree - mid
    # 설정된 mid 값으로 벌목했을 시 구할 수 있는 나무의 총길이를 구한다.
    
    if cnt >= M:
        start = mid + 1
    # 구한 나무의 총길이가 M보다 크거나 같을 경우 mid + 1을 start 값으로 설정해 절단기 높이를 높인다.
    
    else:
        end = mid - 1
    # 구한 나무의 총길이가 M보다 작을 경우 mid - 1을 end 값으로 설정해 절단기 높이를 낮춘다.

print(end)
# start 값이 end를 넘어서는 순간, 즉 반복문이 종료되는 순간이 필요한 나무의 길이를 충족하는 절단기의 최대 높이이므로 end 값을 출력한다.
