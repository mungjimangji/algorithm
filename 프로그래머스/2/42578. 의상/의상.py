from collections import Counter
def solution(clothes):
    answer = 1
    stack = []
    for _, i in clothes:
        stack.append(i)
    clothes_Counter = Counter(stack)
    # print(clothes_Counter.values())
    for j in clothes_Counter.values():

        answer *= j+1
    answer -= 1
    return answer