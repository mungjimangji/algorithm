N, M = map(int, input().split())
num_list = list(map(int, input().split()))
visited = [False]*(N+1)
num_list.sort()
result = []
def backTracking(stack):
    if len(stack) == M:
        n_stack = []
        for s in stack:
            n_stack.append(s)
        if n_stack not in result:
            result.append(n_stack)
            # print(result)
        return
    for i in range(len(num_list)):
        if visited[i] == False and (len(stack)==0 or num_list[i] >= stack[-1]): 
            visited[i] = True 
            stack.append(num_list[i])
            backTracking(stack)
            visited[i] = False
            stack.pop()
    
backTracking([])
for r in result:
    print(*r)