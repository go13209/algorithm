from collections import deque

def solution(n, wires):    
    answer = 100

    for i in range(n-1):
        wire = wires[:i] + wires[i+1:]

        graph = [[] for _ in range(n + 1)]
        for a, b in wire:
            graph[a].append(b)
            graph[b].append(a)

        node = []
        for j in range(1, n + 1):
            visited = [False] * (n + 1)
            node_num = deque([j])
            visited[j] = True

            lst = []

            while node_num:
                num = node_num.popleft()
                lst.append(num)

                for k in graph[num]:
                    if not visited[k]:
                        node_num.append(k)
                        visited[k] = True
            node.append(visited.count(True))

        if max(node) - min(node) < answer:
            answer = max(node) - min(node)

    return answer