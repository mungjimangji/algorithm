numbers = list(map(int, input().split()))

numbers.sort()
numbers.pop()
print(numbers.pop())