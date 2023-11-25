N,I = map(int, input().split())
 
li = []
 
for _ in range(N):
    handle = input()
    li.append(handle)
li.sort()
 
print(li[I-1])