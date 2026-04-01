def solution(x, n):
    answer = []
    #end = (n*x+1) if x > 0 else n+1 if x == 0 else (n*x-1)
    #end = (n*x+1) if x > 0 else (n*x-1)
    #for i in range(x, end, x):
        #answer.append(i)
    #return answer
    
    
    if x > 0:
        for i in range(x, n*x+1, x):
            answer.append(i)
        return answer
    elif x == 0:
        for i in range(n):
            answer.append(x)
        return answer
    else:
        for i in range(x, n*x-1, x):
            answer.append(i)
        return answer