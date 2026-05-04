def solution(s):
    result = []
    for i in range(len(s)):
        if i == 0:
            result.append(s[i].upper())
        elif s[i-1] == ' ':
            result.append(s[i].upper())
        else:
            result.append(s[i].lower())
    return ''.join(result)