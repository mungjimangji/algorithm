T = int(input())
for _ in range(T):
    N = int(input())
    max = 0
    mName = ""
    for _ in range(N):
        name, num = input().split()
        num = int(num)
        if(num > max):
            max = num
            mName = name
    print(mName)
#출처: https://eugene-lab.tistory.com/26 [프로그래밍 일지:티스토리]