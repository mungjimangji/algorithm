N = int(input())
sum = 0
result = 0
sum_number_list = list(map(int, input().split()))

for i in range(N):
    if sum_number_list[i] == 1:
        sum += 1
        result += sum
    else:
        sum = 0

print(result)
