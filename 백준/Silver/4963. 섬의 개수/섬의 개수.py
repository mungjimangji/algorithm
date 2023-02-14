dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    else:

        graph = [list(map(int, input().split())) for _ in range(h)]
        visited = [[False] * w for _ in range(h)]
        # print(graph)
        # print(visited)
        
        cnt = 0
        
        for i in range(h):
            while False in visited[i]:
                start = visited[i].index(False) # 시작 노드
                visited[i][start] = True # 시작 정점 방문 처리 pop을 쓰기위해 스택을 [()]함
                if graph[i][start] == 1:
                    stack = [(i, start)] # 돌아갈 곳을 기록
                    # print(stack)
                    while True: # 스택이 빌 때까지(돌아갈 곳이 없을때까지) 반복
                        if stack == []:
                            cnt += 1
                            break
                        else:
                            cur = stack.pop() # 현재 방문 정점(후입선출)
        
                            for n in range(8):
                                if graph[cur[0]][cur[1]] == 1:
                                    # print(cur)
                                    x = cur[0]
                                    y = cur[1]
                                    for move in range(8):
                                        new_x = dx[move] + x
                                        new_y = dy[move] + y
                                        if 0 <= new_x < h and 0 <= new_y < w:
                                            # print(new_x, new_y)
                                            if graph[new_x][new_y] == 1:
                                                if not visited[new_x][new_y]: # visited가 False이면(방문하지 않았으면)
                                                    visited[new_x][new_y] = True
                                                    stack.append((new_x, new_y))
                                                    # print(stack)
                                                    # print(visited)
        
        print(cnt)