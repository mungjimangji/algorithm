import sys
n = int(input())
result = []
for _ in range(n): 
    result.append(int(sys.stdin.readline()))
result.sort()
for i in result:
    print(i)