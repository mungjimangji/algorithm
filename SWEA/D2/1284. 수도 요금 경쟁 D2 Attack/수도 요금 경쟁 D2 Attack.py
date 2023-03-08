T = int(input())

for t in range(1, T+1):
    result = []
    P, Q, R, S, W = map(int, input().split())
    result.append(P*W)
    if W > R:
        result.append(Q+((W-R)*S))
    else:
        result.append(Q)
    a = min(result)
    print(f"#{t} {a}")