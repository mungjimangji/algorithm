num_list = input().split()

result = []
for num in num_list:
    num = num[::-1]
    num = int(num)
    result.append(num)
print(max(result))