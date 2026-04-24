def solution(t, p):
    arr = []
    result = 0
    l = len(p)
    i = 0
    while True:
        arr.append(int(t[i:l]))
        if len(t) - len(p) == i:
            break
        i += 1
        l += 1
    
    for j in arr:
        if j <= int(p):
            result += 1
    
    return result