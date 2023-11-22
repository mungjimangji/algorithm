def solution(phone_book):
    answer = True
    phone_book.sort()
    # 정렬하면 다음 값이 더 길어야만 포함가능 함
    for i in range(len(phone_book) - 1):
        if phone_book[i] < phone_book[i+1]:
            if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
                answer = False
                return answer
        
        
            
    return answer