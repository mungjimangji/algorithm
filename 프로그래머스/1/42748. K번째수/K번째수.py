def solution(array, commands):
    answer = []
    for c in commands:
        i, j , k = c
        numbers = array[i-1:j]
        numbers.sort()
        answer.append(numbers[k-1])
    
    
    return answer