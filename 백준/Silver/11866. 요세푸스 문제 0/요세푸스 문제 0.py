n, k = map(int, input().split())
num_list = []
for i in range(1, n+1):
    num_list.append(i)
result = []
start = k-1
new_start = k-1

while len(num_list) != 1:
    cur = num_list.pop(start)
    n = len(num_list)
    result.append(cur)
    # print(start)
    # print(result)
    # print(num_list)
    start += k-1
    while start > (n-1):
        # print("if",new_start)
        start = start - n
result.append(num_list.pop())

print("<", end="")
print(*result,sep=", ",end="")
print(">")