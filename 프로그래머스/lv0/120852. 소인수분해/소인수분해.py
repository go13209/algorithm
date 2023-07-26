def solution(n):
    lst = []
    num = 2
    while n != 1:
        if n % num == 0:
            lst.append(num)
            n //= num
        else:
            num += 1
    answer = sorted(list(set(lst)))
    return answer