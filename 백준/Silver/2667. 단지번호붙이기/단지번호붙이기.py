N = int(input())
graph = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(N):
    number = input()
    number = list(map(int, number))
    graph.append(number)
result_dict = {}
stack = []
cnt = 0
for i in range(N):
    for j in range(N):
        # 방문하지 않고 집인 경우에만
        if graph[i][j] != 0:
            # 다시 돌지 않게 0으로 만들어주고
            graph[i][j] = 0
            stack.append((i,j))
            result_dict[cnt+1] = 1
            while stack:
                x,y  = stack.pop()
                for n in range(4):
                    n_x = x + dx[n]
                    n_y = y + dy[n]
                    # 범위 안에 있고, 집이면
                    if 0 <= n_x < N and 0 <= n_y < N and graph[n_x][n_y] == 1:                       
                        graph[n_x][n_y] = 0
                        stack.append((n_x,n_y))
                        result_dict[cnt+1] += 1                            
            cnt += 1

print(len(result_dict))
# result = sorted(result.items(), key=lambda x: (-x[1],-len(x[0]),x[0]))
result = sorted(result_dict.values())
for r in result:
    print(r)