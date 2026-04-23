def solution(n, m):
    answer = []
    a = 0
    b = 0
    for i in range(1, m+1):
        if n % i == 0 and m % i == 0 :
            a = i
            
    b = (n // a) * (m // a) * a

    answer = a, b
    return answer
