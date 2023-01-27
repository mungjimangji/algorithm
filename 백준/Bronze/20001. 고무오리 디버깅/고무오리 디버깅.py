duck_list = []
a = input()
while True:
    duck = input()
    if duck == "문제":
        duck_list.append(duck)
    elif duck == "고무오리":
        if duck_list == []:
            duck_list.append("문제")
            duck_list.append("문제")
        else:
            duck_list.pop()
    elif duck == "고무오리 디버깅 끝":
        break
if duck_list == []:
    print("고무오리야 사랑해")
else:
    print("힝구") 