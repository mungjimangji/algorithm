T = int(input())
while T > 0 :
    a, b, c = map(int, input().split())
    print(min(a, min(b, c)))
    T -= 1
#출처: https://calkolab.tistory.com/entry/baekjoon-python-25494 [CALKO LAB:티스토리]