from collections import Counter

def solution(participant, completion):
    
    dict_result = Counter(participant) - Counter(completion)
   
    answer = list(dict_result.keys())[0]
    return answer