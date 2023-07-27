def solution(balls, share):
    a = 1
    b = 1
    for i in range(balls, balls-share, -1):
        a *= i
    
    for j in range(1, share+1):
        b *= j
        
    return a//b