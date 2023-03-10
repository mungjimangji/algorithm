import re

def solution(babbling):
    answer = 0
    regex = re.compile(r'^(aya|ye|woo|ma)+$')

    for word in babbling:
        if regex.match(word):
            answer += 1

    return answer
