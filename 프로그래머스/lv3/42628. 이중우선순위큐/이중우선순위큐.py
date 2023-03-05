import heapq

def solution(operations):
    heap = []

    for i in operations:
        a, b = i.split()

        if a == 'I':
            heapq.heappush(heap, int(b))

        if a == 'D':
            if b == '1':
                try:
                    heap.remove(max(heap))
                except:
                    continue
            else:
                try:
                    heapq.heappop(heap)
                except:
                    continue

    if len(heap) == 0:
        answer = [0,0]
    else:
        answer = [max(heap), heapq.heappop(heap)]
        
    return answer