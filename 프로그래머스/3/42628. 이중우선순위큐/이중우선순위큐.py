def solution(operations):
    answer = []
    queue=[]

    for oper in operations:
        com,num=oper.split(" ")
        queue.sort()
        if com=="I":
            queue.append(int(num))
        elif com=="D":
            if len(queue)>0:
                if num=="1":
                    queue.remove(int(queue[-1]))
                elif num=="-1":
                    queue.remove(int(queue[0]))

    if len(queue)==0:
        answer.append(0)
        answer.append(0)
    else:
        answer.append(max(queue))
        answer.append(min(queue))

    return answer