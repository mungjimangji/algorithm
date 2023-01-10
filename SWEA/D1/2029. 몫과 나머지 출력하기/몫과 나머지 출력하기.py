
T = int(input())

for t in range(1, T+1):
    a, b = map(int, input().split())
    quotient = a // b
    remainder = a % b
    print("#{0} {1} {2}".format(t, quotient, remainder))
