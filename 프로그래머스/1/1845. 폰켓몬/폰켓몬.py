from collections import Counter
def solution(nums):
    list_len = len(nums)
    nums = Counter(nums)
    Counter_len = len(nums)
    if list_len / 2 < Counter_len:
        answer = list_len / 2
    else:
        answer = Counter_len
    
    
    return answer