def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x:x[1])
    camera = -30001

    for i in range(len(routes)):
        if routes[i][0] <= camera:
            continue
        else:
            answer += 1
            camera = routes[i][1]
    return answer