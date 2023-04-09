def solution(n, costs):
    costs = sorted(costs, key=lambda x:x[2])
    connected = set([costs[0][0], costs[0][1]])
    answer = costs[0][2]
    
    while len(connected) != n:
        for i in range(1, len(costs)):
            if costs[i][0] in connected and costs[i][1] in connected:
                continue
            if costs[i][0] in connected or costs[i][1] in connected:
                connected.add(costs[i][0])
                connected.add(costs[i][1])
                answer += costs[i][2]
                break
    return answer