import sys
import heapq

heap = []

for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())

    if num == 0:
        try:
            print(-heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, -num)