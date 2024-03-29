import sys
input = sys.stdin.readline

# 최소 길이 출력, 불가능 하면 0 출력
N, S = map(int, input().split())
sequence = list(map(int, input().split()))

min_length = N+1
start, end = 0, 0
partial_sum = 0


while True:
    
    if partial_sum >= S:
        if min_length > end - start:
            min_length = end - start
        partial_sum -= sequence[start]
        start += 1
    elif end == N:
        break
    else:
        partial_sum += sequence[end]
        end += 1

if min_length != N+1:
    print(min_length)
else:
    print(0)