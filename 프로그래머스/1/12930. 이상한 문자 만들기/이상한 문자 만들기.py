def solution(s):
    arr = list(s)
    answer = ''
    i = 0
    while True:
        if i % 2 == 0:
            answer = answer + arr[i].upper()
        else:
            answer = answer + arr[i].lower()
        if arr[i] == ' ':
            del arr[0:i+1]
            i = -1
        if i == len(arr) - 1:
            break
        i += 1
    return answer
        
        