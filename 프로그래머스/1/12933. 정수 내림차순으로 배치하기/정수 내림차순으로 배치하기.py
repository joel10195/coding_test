def solution(n):
    answer = ''
    l = []
    str_n = str(n)
    for i in str_n:
        l.append(i)
    l.sort(reverse=True)
    
    for j in l:
        answer = answer + j
    return int(answer)
