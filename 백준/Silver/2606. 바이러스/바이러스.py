n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

# 인접 리스트 만들기
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


start = 1 # 시작 노드
stack = [start] # 돌아갈 곳을 기록
visited[start] = True # 시작 정점 방문 처리
while stack: # 스택이 빌 때까지(돌아갈 곳이 없을때까지) 반복
    cur = stack.pop() # 현재 방문 정점(후입선출)

    for i in graph[cur]:
        if not visited[i]: # visited가 False이면(방문하지 않았으면)
            visited[i] = True
            stack.append(i)
print(sum(visited)-1)
