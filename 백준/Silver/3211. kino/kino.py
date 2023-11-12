n = int(input())
a = [int(input()) for _ in range(n)]
a.sort()

result = 1
while result <= n and a[result - 1] + 1 > result:
    result = a[result - 1] + 1

print(result)