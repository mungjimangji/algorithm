T = int(input())

for t in range(T):
    scores_list = list(map(int, input().split()))
    scores_list = scores_list[1:]
    score_avg = sum(scores_list) / len(scores_list)
    cnt = 0
    for score in scores_list:
        if score > score_avg:
            cnt += 1
    student_avg = cnt / len(scores_list) * 100
    print("{0:.3f}%".format(student_avg))