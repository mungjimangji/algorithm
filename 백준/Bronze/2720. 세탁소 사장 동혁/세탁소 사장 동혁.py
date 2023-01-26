T = int(input())
for t in range(T):
    C = int(input())

    Quarter = C // 25
    Q = C % 25
    Dime = Q // 10
    D = Q % 10
    Nickel = D // 5
    N = D % 5
    Penny = N // 1
    P = N % 1
    
    print(Quarter, Dime, Nickel, Penny)
