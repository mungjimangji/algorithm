T = int(input())
ball = [1, 0, 0]
result = [0, 0, 0]
for _ in range(T):
    x, y = map(int, input().split())
    if x > 3 and y > 3:
        print(-1)
        break
    else:
        ball[x-1], ball[y-1] = ball[y-1], ball[x-1]
            
print(ball.index(1) + 1)