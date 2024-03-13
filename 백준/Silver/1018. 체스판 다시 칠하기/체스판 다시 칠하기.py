# 체스판 만들기
N, M = map(int, input().split())
chats = []

for _ in range(N):
    c = list(input())
    chats.append(c)
result = 64
for a in range(N-7):
    for b in range(M-7):
        # print(a,b)
        index1 = 0 # 홀수가 W인 경우 짝수가 B인경우
        index2 = 0 # 짝수가 W인 경우 홀수가 B인경우

        for i in range(a, 8+a):
            for j in range(b, 8+b):
                # print(i,j)
                if (i + j) % 2: # 두개 더해서 홀수인 경우 ex) (0,1)
                    if chats[i][j] == "B":
                        index1 += 1
                    elif chats[i][j] == "W":
                        index2 += 1
                else: # 두개 더해서 짝수일 경우
                    if chats[i][j] == "B":
                        index2 += 1
                    elif chats[i][j] == "W":
                        index1 += 1

        result = min(result, index1, index2)
print(result)
