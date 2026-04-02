def solution(s):
    pp = 0
    yy = 0
    
    for i in s:
        if i == "p" or i == "P":
            pp = pp + 1
        elif i == "y" or i == "Y":
            yy = yy + 1
            
    return pp == yy