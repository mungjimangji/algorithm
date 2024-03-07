from collections import deque

N, M, V = map(int, input().split())

graph = []
for _ in range(N+1):
    graph.append([])

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()

dfs_visited = [0] * (N+1)
bfs_visited = [0] * (N+1)

def dfs(graph, start, visited):
    stack = [start]
    result = []

    while stack:
        cur = stack.pop()

        if visited[cur]:
            continue

        visited[cur] = 1
        result.append(cur)

        for i in sorted(graph[cur], reverse=True):
            if visited[i] == 0: # 방문하지 않는 노드만 방문
                stack.append(i)

    print(*result)

def bfs(graph, start, visited):
    # print(graph)
    result = []
    queue = deque([start])
    visited[start] = 1

    while queue:
        cur  = queue.popleft()
        result.append(cur)
        # print(graph[cur])
        for i in graph[cur]:
            # print(i)
            if visited[i] == 0: # 방문하지 않았으면
                queue.append(i)
                visited[i] = 1
    print(*result)


dfs(graph, V, dfs_visited)
bfs(graph, V, bfs_visited)