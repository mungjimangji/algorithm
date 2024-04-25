n=int(input())
arr=list(map(int,input().split()))

high=0#제일 높은 봉우리
cnt=0#사냥꾼이 잡을 수 있는 수
total=[]#전체 저장

for i in arr:
    if i>high:#가장 높은 값보다 배열이 크면
        high=i#해당값을 바꾸고(최댓값 구하기)
        cnt=0#0으로 초기화
    else:#아니라면
        cnt+=1#용을 사냥할 수 있으므로 1증가
    total.append(cnt)#배열에 추가
print(max(total))#가장 큰 값 출력
# 데일리