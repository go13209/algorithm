def solution(s):
    lst = []
    for i in range(len(s)):
        if s[i] == '(':
            lst.append(s[i])
        else:
            try:
                lst.pop()
            except:
                answer = False
                break
    else:
        if lst:
            answer = False
        else:
            answer = True

    return answer