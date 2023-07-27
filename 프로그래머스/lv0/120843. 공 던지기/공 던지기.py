def solution(numbers, k):
    cnt = 1
    idx = 0
    while cnt != k:
        cnt += 1
        idx += 2
        if idx >= len(numbers):
            idx -= len(numbers)
        
    return numbers[idx]