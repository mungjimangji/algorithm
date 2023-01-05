a = input()
b = input()
result = []
for i in b:
    result.append(int(i) * int(a))
print(result[2])
print(result[1])
print(result[0])
print((result[0] * 100) + (result[1] * 10) + result[2])