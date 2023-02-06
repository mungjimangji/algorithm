result = []
station = 0
for _ in range(4):
    lower, ride = map(int, input().split())
    station = station + ride - lower
    result.append(station)

print(max(result))