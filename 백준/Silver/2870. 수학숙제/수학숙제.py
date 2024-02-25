numbers = []
N = int(input())

for _ in range(N):
    string = input()
    # 문자열을 하나씩 돌면서 숫자일 경우 변수에 더해줌
    # 숫자일 경우엔 변수를 초기화 시키고 리스트에 넣어주기
    cnt = ""
    for s in string:
        # 숫자이면
        if s.isdigit():
            cnt += s
        # 문자열이면
        else:
            if cnt: # 숫자가 담겨 있으면
                numbers.append(int(cnt))
                cnt = ""
    # 마지막까지 숫자인 경우
    if cnt:
        numbers.append(int(cnt))
numbers.sort()
for num in numbers:
    print(num)