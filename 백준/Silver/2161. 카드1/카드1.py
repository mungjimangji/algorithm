N = int(input())
numbers = list(range(1, N+1))
pop_numbers = []
while 1 < len(numbers):
    print(numbers.pop(0), end=" ")
    numbers.append(numbers.pop(0))
print(*numbers)