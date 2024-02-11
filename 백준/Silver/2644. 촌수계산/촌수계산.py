from collections import deque

N = int(input())
a, b = map(int, input().split())
M = int(input())
relation = []
visited = [0] * (N+1)
for _ in range(N+1):
    relation.append([])

d = deque([a])
for _ in range(M):
    x, y = map(int, input().split())
    relation[x].append(y)
    relation[y].append(x)
check = 0
while d:
    cur = d.popleft()
    
    # print(cur)
    if cur == b:
        print(visited[cur])
        check = 1
        break
    for i in relation[cur]:
        if visited[i] == 0:
            d.append(i)
            visited[i] = visited[cur] + 1
            # print(visited)

if check == 0:
    print(-1)