a, b = map(int, input().split())
print(a + b)
while a + b > 0:
    a, b = map(int, input().split())
    if a + b == 0:
        break
    else:
        print(a + b)