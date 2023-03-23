def plus(X, Y):
    return int(X) + int(Y)


def minus(X, Y):
    return int(X) - int(Y)


def calculator(X, Y, operator):
    calc_dict = {
        "+": plus, "-": minus
    }
    
    return calc_dict[operator](X, Y)
    

def solution(quiz_list):
    answer = []
    
    for quiz in quiz_list:
        X, operator, Y, equal, Z = quiz.split()
        
        if calculator(X=X, Y=Y, operator=operator) == int(Z):
            answer.append("O")
        else:
            answer.append("X")
        
    return answer