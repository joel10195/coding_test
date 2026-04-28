def solution(n):
    result = 0
    answer = ''
    while True:
        if n == 0:
            break
        if n % 3 == 0:
            answer = str(0) + answer
        else:
            answer = str(int(n%3)) + answer
        n = n // 3
    
    arr = list(answer)
    
    for i in range(len(answer)):
        result = result + int(arr[i]) * (3 ** i)
    return result
