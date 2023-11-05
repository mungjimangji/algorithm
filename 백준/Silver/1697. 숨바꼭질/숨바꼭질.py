from collections import deque

N, K = map(int, input().split())
visited = [0] * 1000001
stack = deque([N])


while stack:
    cur = stack.popleft()
    if cur == K:
        print(visited[cur])
        break
    for i in (cur + 1, cur - 1, cur * 2):
        if 0 <= i <= 100000 and visited[i] == 0:
            visited[i] = visited[cur] + 1
            stack.append(i)