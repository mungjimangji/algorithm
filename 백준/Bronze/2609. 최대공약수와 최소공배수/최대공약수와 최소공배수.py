a, b = map(int, input().split())
n = 2
result_list = []
result_2_list = []
while True:
    if n > a or n > b:
        result_2_list.append(a)
        result_2_list.append(b)
        break
    else:
        if a % n == 0 and b % n == 0:
            result_list.append(n)
            a = a // n
            b = b // n
        else:
            n += 1
result = 1
result_2 = 1
for i in result_list:
    result *= i
for j in result_2_list:
    result_2 *= j
print(result)
print(result*result_2)