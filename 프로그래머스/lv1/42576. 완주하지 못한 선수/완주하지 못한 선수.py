def solution(participant, completion):
    participant.sort()
    completion.sort()
    for _ in range(len(completion)):
        p_name = participant.pop()
        c_name = completion.pop()
        if p_name == c_name:
            continue
        else:
            answer = p_name
            break
    else:
        answer = participant[0]
    
    return answer
            