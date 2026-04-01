def solution(n):
    s = str(n)
    answer = []
    for i in s:
        answer.append(int(i))
     
    answer.reverse()
    return answer