from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
N, M, K = map(int, input().split())
food = []

for _ in range(N):
    food.append([0] * M)

for k in range(K):
    a, b = map(int, input().split())
    food[a-1][b-1] = 1
result = 0
for i in range(N):
    for j in range(M):
        if food[i][j] == 1:
            deq = deque([(i, j)])
            food[i][j] = 0
            cnt = 1
            while deq:
                x, y = deq.popleft()
                for n in range(4):
                    nx = x + dx[n]
                    ny = y + dy[n]
                    if 0 <= nx < N and 0 <= ny < M:
                        if food[nx][ny] == 1:
                            deq.append((nx, ny))
                            cnt += 1
                            food[nx][ny] = 0
            result = max(result, cnt)
print(result)