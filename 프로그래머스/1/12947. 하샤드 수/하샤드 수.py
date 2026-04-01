def solution(x):
    hap = 0
    s = str(x)
    for i in s:
        hap = hap + int(i)
    if x % hap == 0:
        return 1 == 1
    else:
        return 1 == 0