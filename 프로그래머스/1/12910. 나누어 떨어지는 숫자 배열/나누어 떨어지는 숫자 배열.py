def solution(arr, divisor):
    result = []
    m_result = [-1]
    for i in arr:
        if i % divisor == 0:
            result.append(i)
    result.sort()
    if sum(result) == 0:
        return m_result
    return result