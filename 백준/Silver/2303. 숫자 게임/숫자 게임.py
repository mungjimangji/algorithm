N = int(input())
best_scores = []

for i in range(N):
    cards = list(map(int, input().split()))
    max_digit = 0

    for one in range(5):
        for two in range(one + 1, 5):
            for three in range(two + 1, 5):
                temp = (cards[one] + cards[two] + cards[three]) % 10
                if max_digit < temp:
                    max_digit = temp

    best_scores.append(max_digit)

best = max(best_scores)

for i in range(N - 1, -1, -1):
    if best == best_scores[i]:
        print(i + 1)
        break


