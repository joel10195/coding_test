def solution(s):
    result = [-1]
    arr = list(s)
    for i in range(1, len(arr)):
        for k in range(i-1, -1, -1):
            if arr[i] == arr[k]:
                result.append(i-k)
                break
            elif k == 0:
                result.append(-1)
            
    
        
    
    return result