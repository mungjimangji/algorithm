N = int(input())
guests = map(int, input().split())
result = []
cnt = 0
for guest in guests:
    if guest in result:
        cnt += 1
    else:
        result.append(guest)
print(cnt)