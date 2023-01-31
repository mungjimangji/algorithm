matrix = []
for _ in range(5):
    a = list(input())
    matrix.append(a)
maxx = 0
for m in matrix:
    if maxx < len(m):
        maxx = len(m)

for i in range(maxx):
    for j in range(5):
        try:
            print(matrix[j][i], end="")
        except:
            continue