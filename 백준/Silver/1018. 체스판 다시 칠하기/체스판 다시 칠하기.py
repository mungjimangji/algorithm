N ,M = map(int, input().split())

graph = []
for _ in range(N):
    string = list(input())
    graph.append(string)

result = []
for n in range(N-7): # 가로
    for m in range(M-7): # 세로
        draw1 = 0
        draw2 = 0
        for i in range(8): # 가로 돌기
            for j in range(8): # 세로 돌기
                i_1 = i + n
                j_1 = j + m

                if (i_1 + j_1)  % 2 == 0:
                    if graph[i_1][j_1] == "B":
                        draw1 += 1
                    if graph[i_1][j_1] == "W":
                        draw2 += 1

                else:
                    if graph[i_1][j_1] == "W":
                        draw1 += 1
                    if graph[i_1][j_1] == "B":
                        draw2 += 1
        result.append(draw1)
        result.append(draw2)
print(min(result))