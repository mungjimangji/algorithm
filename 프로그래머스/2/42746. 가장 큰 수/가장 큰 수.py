def solution(numbers):
    numbers = map(str, numbers)
    result = []
    answer = ''
    for n in numbers:
        new_n = n
        i = 0
        while len(new_n) < 4:
            new_n += n[i]
            i += 1
            if i == len(n):
                i = 0
        result.append((new_n, n))
    result = sorted(result, reverse=True)
    # print(result)
    for r in result:
        answer += r[1]
    answer = int(answer)
    answer = str(answer)    
    return answer