s = input()

s = s.replace("pi", " ")
s = s.replace("ka", " ")
s = s.replace("chu", " ")

if len(s.strip()) == 0:
    print("YES")
else:
    print("NO")
#출처: https://woojinhong.tistory.com/153 [홍우진의 개발 일기장:티스토리]