T = int(input())

for t in range(1, T+1):
    
    numbers = list(map(int, input().split()))
    avg = sum(numbers) / len(numbers)
    print("#{0} {1:.0f}".format(t, round(avg, 0)))