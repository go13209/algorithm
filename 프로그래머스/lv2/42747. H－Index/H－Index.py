def solution(citations):
    answer = len(citations)

    while True:
        cnt = len([i for i in citations if i >= answer])
        if cnt >= answer:
            return answer
        else:
            answer -= 1