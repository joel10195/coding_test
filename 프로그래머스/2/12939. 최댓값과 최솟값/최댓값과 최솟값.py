def solution(s):
    arr = []
    result = ''
    for i in s.split(' '):
        arr.append(int(i))
    result = str(min(arr)) + ' ' + str(max(arr))
    return result
        