def solution(left, right):
    arr = []
    result = 0
    for i in range(left, right + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                arr.append(j)
    
        if len(arr) % 2 == 0:
            result = result + i
        else:
            result = result - i
        arr = []
        
    return result