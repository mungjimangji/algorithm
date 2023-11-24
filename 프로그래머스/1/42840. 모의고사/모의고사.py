def solution(answers):
    answer = []
    a_l = len(answers)
    student1 = [1,2,3,4,5] * 2000
    student2 = [2,1,2,3,2,4,2,5] * 1250
    student3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    r_1 = 0
    r_2 = 0
    r_3 = 0
    # if a_l > len(student1):
    #     student1 *= len(student1) // a_l
    #     student1 += len(student1) % a_l
    # if a_l > len(student2):
    #     student2 *= len(student2) // a_l
    #     student2 += len(student2) % a_l
    # if a_l > len(student3):
    #     student3 *= len(student3) // a_l
    #     student3 += len(student3) % a_l
    for i in range(len(answers)):
        if answers[i] == student1[i]:
            r_1 += 1
        if answers[i] == student2[i]:
            r_2 += 1 
        if answers[i] == student3[i]:
            r_3 += 1 
    result = max(r_1, r_2, r_3)
    cnt = 0
    for j in (r_1, r_2, r_3):
        cnt += 1
        if j == result:
            answer.append(cnt)
                
    
    
    
    return answer