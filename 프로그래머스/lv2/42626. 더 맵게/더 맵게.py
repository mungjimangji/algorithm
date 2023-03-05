import heapq
def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    if scoville[0] >= K:
        return cnt
    
    while True:
        if len(scoville) == 1:
            return -1
        num1 = heapq.heappop(scoville)
        num2 = heapq.heappop(scoville)
        result = num1 + num2 * 2
        heapq.heappush(scoville, result)
        cnt += 1
        if scoville[0] >= K:
            return cnt    
           
    return cnt