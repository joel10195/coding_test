def solution(a, b):
    small = min(a, b)   #3
    big = max(a, b)     #5
    result = 0
    
    for i in range(small, big+1):
        result = result + i
        
    return result