T = int(input())
string = []
for t in range(T):
    R, S = input().split()
    
    for s in S:
       string.append(s * int(R))
    print("".join(string))
    string = []