# 백준 1654 랜선 자르기

import sys

K, N = map(int, sys.stdin.readline().split())

lan = [int(sys.stdin.readline()) for _ in range(K)]
start = 1
end = max(lan)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for l in lan:
        total += l // mid
    
    if total >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)
