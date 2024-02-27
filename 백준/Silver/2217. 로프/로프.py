import sys
N = int(input())
numbers = []

for _ in range(N):
    num = int(sys.stdin.readline())
    numbers.append(num)
numbers.sort()

# 정렬된 리스트를 반복문으로 돌려서 최댓값을 구해준다.
cnt = 0
result = []
while cnt < N:
    result.append(numbers[cnt] * (N - cnt))
    cnt += 1
print(max(result))