def solution(numer1, denom1, numer2, denom2):
    answer = []
    d3 = denom1 * denom2
    n3 = numer1 * d3 // denom1 + numer2 * d3 // denom2

    i = 2
    while i <= d3:
        if n3 % i == 0 and d3 % i == 0:
            n3 //= i
            d3 //= i
        else:
            i += 1
    
    answer.append(n3)
    answer.append(d3)
        
    return answer