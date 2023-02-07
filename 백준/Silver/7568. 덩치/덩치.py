N = int(input())

result_list = []
for _ in range(N):
    xy = list(map(int, input().split()))
    result_list.append(xy)

result_dict = {}
for n in range(1, N+1):
    result_dict[n] = 1

for i in range(N):
    for j in range(N):
        if result_list[i][0] < result_list[j][0] and result_list[i][1] < result_list[j][1]:
            result_dict[i+1] += 1
        # elif result_list[i][0] > result_list[j][0] and result_list[i][1] > result_list[j][1]:
        #     result_dict[j+1] += 1

print(*result_dict.values())