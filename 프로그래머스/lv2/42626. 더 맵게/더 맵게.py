import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) < 2:
            answer = -1
            break
        else:
            least = heapq.heappop(scoville)
            least_2 = heapq.heappop(scoville)

            heapq.heappush(scoville, least + least_2 * 2)
            answer += 1
    
    return answer