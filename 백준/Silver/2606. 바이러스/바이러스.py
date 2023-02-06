import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

infected = [False] * (N + 1)
start = 1

stack = [start]
infected[start] = True

while stack:
    com_num = stack.pop()

    for adj in graph[com_num]:
        if not infected[adj]:
            infected[adj] = True
            stack.append(adj)

print(infected.count(True) - 1)