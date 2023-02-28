import math

def solution(progresses, speeds):
    days = []
    answer = []
    
    for i in range(len(progresses)):
        take_time = math.ceil((100 - progresses[i]) / speeds[i])
        
        if i == 0:
            days.append(take_time)
        else:
            if take_time <= days[0]:
                days.append(take_time)
            else:
                answer.append(len(days))
                days.clear()
                days.append(take_time)
    answer.append(len(days))
                
    return answer