import sys
# sys.stdin  = open('input.txt', 'r')
from collections import deque

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

visited = [False] * len(numbers)


left, right = 0, 0 # 두 개의 포인터는 0에서 부터 시작
total = 0 # 합을 저장할 변수
min_length = 100000 # 먼저 최대 길이로 지정

while True:
    # 만약 총 합이 S가 넘는다면, left를 하나씩 옮겨보면서 어디까지 길이가 줄어드나 확인
    if total >= S:
        min_length = min(min_length, right - left)
        total -= numbers[left]
        left += 1
    elif right == N:
        break
    # 만약 총합이 S를 넘지 않는다면, right 을 오른쪽으로 한칸씩 옮기며 총합이 S를 넘을때까지 더함
    else:
        total += numbers[right]
        right += 1

if min_length == 100000:
    print(0)
else:
    print(min_length)