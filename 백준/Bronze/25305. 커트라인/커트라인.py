N, K = map(int, input().split())
num_list = list(map(int, input().split()))

result = []
for _ in range(K):
    a = max(num_list)
    b = num_list.index(max(num_list))
    result.append(a)
    num_list.pop(b)

print(min(result))