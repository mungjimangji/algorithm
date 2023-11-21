from collections import deque
def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    p = deque(participant)
    c = deque(completion)
    check = False
    for i in range(len(c)):
        a = p.popleft()
        if c[i] != a:
            answer = a
            return answer
    
    answer = p.pop()
            
            
    return answer