N = int(input())
trees = list(map(int, input().split()))
lemon = [trees[i] - (N - i) for i in range(N)]  # 이동하면서 흘린 레몬 개수 차감

print(max(lemon))