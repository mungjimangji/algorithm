a, b = map(int, input().split())
c = int(input())

minute = b + c

if b + c >= 60:
    minute_new = minute % 60
    a = a + (minute // 60)
    if a >= 24:
        a -= 24
else:
    minute_new = minute       
print(a, minute_new)