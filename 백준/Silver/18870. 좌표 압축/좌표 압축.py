N = int(input())
numbers = list(map(int, input().split()))
result = []
check = list(set(numbers))
check.sort()
dic = {}

for i in range(len(check)):
    dic[check[i]] = i

for num in numbers:
    result.append(dic[num])
print(*result)