# 백준 DFS와 BFS

from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in graph:
    i.sort()

def dfs(start):
    visited_dfs[start] = True
    print(start, end=' ')

    for j in graph[start]:
        if not visited_dfs[j]:
            dfs(j)


def bfs(start):
    queue = deque([start])
    visited_bfs[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for n in graph[node]:
            if not visited_bfs[n]:
                visited_bfs[n] = True
                queue.append(n)

dfs(V)
print()
bfs(V)