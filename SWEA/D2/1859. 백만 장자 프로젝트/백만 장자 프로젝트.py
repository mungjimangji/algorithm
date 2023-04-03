T = int(input())
for t in range(1, T+1):
    stack = []
    result = 0
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers = numbers[::-1]
    max_num = numbers[0]
    for i in range(1, len(numbers)):
        if max_num > numbers[i]:
            result +=  max_num - numbers[i]
        elif max_num <= numbers[i]:
            max_num = numbers[i]   

    print(f"#{t} {result}")
