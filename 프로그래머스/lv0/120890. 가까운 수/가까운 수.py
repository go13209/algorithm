import heapq

def solution(array, n):
    heap = []
    for num in array:
        heapq.heappush(heap, (abs(n-num), num))
    answer = heap[0][1]
    return answer