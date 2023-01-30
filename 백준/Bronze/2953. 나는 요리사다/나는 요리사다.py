result_list = []
for _ in range(5):
    a = list(map(int, input().split()))
    result_list.append(sum(a))
result_max = max(result_list)
print(result_list.index(result_max)+1, result_max)