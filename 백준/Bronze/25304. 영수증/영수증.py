X = int(input())
T = int(input())
X_sum = 0
for t in range(1, T+1):
    a, b = map(int, input().split())
    X_sum += a * b

if X == X_sum:
    print("Yes")
else:
    print("No")