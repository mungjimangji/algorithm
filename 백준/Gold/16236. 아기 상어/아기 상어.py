from collections import deque

N = int(input())
sea = []
for _ in range(N):
    graph = list(map(int, input().split()))
    sea.append(graph)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 상어 위치 찾기
for n in range(N):
    if 9 in sea[n]:
        shark_x = n
        shark_y = sea[n].index(9)
        sea[shark_x][shark_y] = 0

baby_size = 2
total_days = 0
eat = 0
while True:
    q = deque()
    q.append((shark_x, shark_y, 0))
    visited = [[False] * N for _ in range(N)]
    flag = 1e9
    fish = []

    while q:
        x, y, count = q.popleft()

        # 먹을 수 있는 상어가 없으면 while문 종료
        if count > flag:
            break
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 상하좌우가 범위 안에 있는 경우와
            if 0 <= nx < N and 0 <= ny < N: 
                # 아직 방문하지 않은 경우
                if visited[nx][ny] == False and sea[nx][ny] <= baby_size: 
                    # 0이 아니고 상어보다 작거나 같은 경우
                    if 0 < sea[nx][ny] < baby_size:
                        fish.append((nx, ny, count + 1)) # fish에 넣어주고
                        flag = count

                    # 0이고 상어보다 커도 다시 방문하지 않기 위해서 방문리스트 초기화
                    visited[nx][ny] = True
                    q.append((nx, ny, count + 1))

    # 이동 횟수가 같은 물고기 들이 여러마리면 아래 코드로
    if len(fish) > 0:
        fish.sort()
        x, y, move = fish[0][0], fish[0][1], fish[0][2]
        total_days += move
        eat += 1
        sea[x][y] = 0 # 잡아먹힘
        if eat == baby_size:
            baby_size += 1
            eat = 0
        shark_x, shark_y = x, y
    else:
        break
print(total_days)    