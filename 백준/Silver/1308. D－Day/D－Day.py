import datetime
a, b, c = map(int, input().split())
start = datetime.date(a, b, c)
temp = datetime.date(a+1000, b, c)
a, b, c = map(int, input().split())
end = datetime.date(a, b, c)
result = (start-end).days
if end >= temp:
    print("gg")
else:
    print('D'+str(result))