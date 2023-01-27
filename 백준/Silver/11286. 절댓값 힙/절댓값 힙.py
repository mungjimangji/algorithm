import sys
import heapq

N = int(input())
numbers = []
for _ in range(N):
    number = int(sys.stdin.readline())
    if number != 0:
        heapq.heappush(numbers, (abs(number), number))
    else:
        if numbers:
            
            result = heapq.heappop(numbers)
            print(result[1])
        else:
            print(0)
