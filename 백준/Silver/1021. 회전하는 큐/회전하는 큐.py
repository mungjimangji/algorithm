N, M = map(int, input().split())
num_deq = list(i for i in range(1, N+1))
num_list = list(map(int, input().split()))
cnt = 0
for i in num_list:
    while True:
        if num_deq[0] == i:
            num_deq.pop(0)
            break
        else:
            n = num_deq.index(i)
            if len(num_deq[:n]) <= len(num_deq[n+1:]):
                a = num_deq.pop(0)
                num_deq.append(a)
                cnt += 1
            else:
                b = num_deq.pop()
                num_deq.insert(0, b)
                cnt += 1
print(cnt)
