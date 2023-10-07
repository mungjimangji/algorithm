T = int(input())
for _ in range(T):
    K = int(input())
    N = int(input())
    people = [i for i in range(1, N+1)]
    for k in range(K):
        for n in range(1, N):
            people[n] += people[n-1]
    print(people[-1])