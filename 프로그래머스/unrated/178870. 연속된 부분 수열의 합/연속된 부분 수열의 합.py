def solution(sequence, k):
    answer = []
    num_sum = 0
    num_start = 0

    for num_end in range(len(sequence)):
        num_sum += sequence[num_end]

        while num_sum > k:
            num_sum -= sequence[num_start]
            num_start += 1

        
        if num_sum == k and (not answer or answer[1] - answer[0] > num_end - num_start):
            answer = [num_start, num_end]

    return answer