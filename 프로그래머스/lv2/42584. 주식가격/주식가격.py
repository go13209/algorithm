from collections import deque

def solution(prices):
    price_deque = deque(prices)
    answer = []
    
    while price_deque:
        p = price_deque.popleft()
        cnt = 0
        for price in price_deque:
            if price >= p:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
        
    return answer