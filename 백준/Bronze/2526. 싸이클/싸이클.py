n, p = map(int, input().split())

list = []
r = n

while True:
    r = (r * n) % p
    if r in list:
        print(len(list) - list.index(r))
        break
    list.append(r)