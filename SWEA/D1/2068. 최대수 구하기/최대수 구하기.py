T = int(input())

for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    numbers_max = max(numbers)
    print("#{0} {1}".format(t, numbers_max))