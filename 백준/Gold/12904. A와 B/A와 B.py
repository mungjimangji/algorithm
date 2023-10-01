S = input()
T = input()

while len(T) > len(S):
    if T[-1] == 'A':
        T = T[:-1]
    else:
        T = T[:-1][::-1]

result = 1 if S == T else 0
print(result)