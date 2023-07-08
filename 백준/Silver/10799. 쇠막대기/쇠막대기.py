marks = input()
count = 0  # 괄호 개수 추적
result = 0  # 결과 값

i = 0
while i < len(marks):
    if marks[i] == '(':
        if marks[i + 1] == ')':  # 레이저인 경우
            result += count  # 현재까지의 쇠막대기 개수를 결과에 추가
            i += 1  # 레이저는 두 글자이므로 다음 글자로 이동
        else:  # 쇠막대기 시작인 경우
            count += 1
    else:  # 쇠막대기의 끝인 경우
        count -= 1
        result += 1  # 끝난 쇠막대기 하나를 결과에 추가

    i += 1

print(result)