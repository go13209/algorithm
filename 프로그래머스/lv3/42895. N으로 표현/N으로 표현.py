def solution(N, number):
    num = [set() for _ in range(9)]

    for i in range(1, 9):
        num[i].add(int(str(N) * i))
        for j in range(1, i):
            for k in num[j]:
                for l in num[i - j]:
                    num[i].add(k+l)
                    num[i].add(abs(k-l))
                    num[i].add(k*l)
                    if k != 0 :
                        num[i].add(l // k)
                    if l != 0 :
                        num[i].add(k // l)
        
        if number in num[i]:
            return i
    
    return -1
