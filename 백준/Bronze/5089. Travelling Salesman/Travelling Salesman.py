cnt = 0
while True:
    cnt += 1
    n = int(input())
    if n == 0:
        break
    t = {input():1 for _ in range(n)}
    print(f'Week {cnt} {len(t.keys())}')