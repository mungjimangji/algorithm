def solution(lines):
    arr = [0 for _ in range(200)]
    answer = 0

    for i in range(len(lines)):
        for j in range(lines[i][0] + 100, lines[i][1] + 100):
            arr[j] += 1

    for i in range(200):
        if arr[i] > 1:
            answer += 1

    return answer