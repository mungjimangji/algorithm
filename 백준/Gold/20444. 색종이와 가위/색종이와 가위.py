n, k = map(int, input().split())
# 이분법으로 차근 차근 나아간다.
# 세로로 자른 경우와 가로로 자른 경우의 차가 작을 경우 조각의 수는 많아지고,
# 클 경우 조각의 수는 적어진다.
left = 0
right = n // 2
isPossible = False

while left <= right:
    rowCut = (left + right) // 2
    colCut = n - rowCut
    # 가로, 세로 각각 rowCut, colCut번씩 잘랐다면 (rowCut + 1) * (colCut + 1) 조각이 생김
    pieces = (rowCut + 1) * (colCut + 1)
    if k == pieces:
        print('YES')
        isPossible = True
        break
    if k > pieces:
        left = rowCut + 1
    else:
        right = rowCut - 1

if not isPossible:
    print('NO')
