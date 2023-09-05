dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

M, N, K = map(int, input().split())

graph = []
for _ in range(M):
    graph.append([0]*N)


for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x2-x1):
        for j in range(y2-y1):
            graph[y1+j][x1+i] = 1

stack = []
result = []
for x in range(N):
    for y in range(M):
        if graph[y][x] == 0:
            cnt = 1
            graph[y][x] = 3
            stack.append((x,y))
            while stack:
                a, b = stack.pop()
                for n in range(4):
                    nx = a + dx[n]
                    ny = b + dy[n]
                    if 0 <= nx < N and 0 <= ny < M and graph[ny][nx] == 0:
                        stack.append((nx,ny))
                       
                        graph[ny][nx] = 3
                        cnt += 1
            result.append(cnt)
result.sort()
print(len(result))
print(*result)