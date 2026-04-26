def solution(number):
    arr = [0, 0, 0]
    result = 0
    for i in range(len(number)):
        arr[0] = number[i]
        
        for j in range(len(number)):
            if j <= i :
                continue
            arr[1] = number[j]
            
            for k in range(len(number)):
                if (k <= i) or (k <= j):
                    continue
                arr[2] = number[k]
                if sum(arr) == 0:
                    result += 1
    return result
        