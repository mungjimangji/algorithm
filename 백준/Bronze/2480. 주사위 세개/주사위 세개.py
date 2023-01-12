a, b, c = map(int, input().split())
numbers_list = [a, b, c]

if a == b == c:
    print(10000 + 1000 * a)

elif a == b or a == c:
    print(1000 + 100 * a)

elif b == c:
    print(1000 + 100 * b)

else:
    numbers_list_max = max(numbers_list)
    print(numbers_list_max * 100)