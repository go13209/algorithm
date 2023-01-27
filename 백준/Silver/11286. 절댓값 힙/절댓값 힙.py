import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if heap:
            print(heap[0][1])
            heapq.heappop(heap)
        else:
            print(0)
    else:
        if num < 0:
            heapq.heappush(heap, (num * -1, num))        
        else:
            heapq.heappush(heap, (num, num))