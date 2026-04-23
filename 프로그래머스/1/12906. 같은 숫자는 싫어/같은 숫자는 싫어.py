def solution(arr):
    answer = []
    
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i])
        elif i == len(arr)-2:
            if arr[i] == arr[i+1]:
                answer.append(arr[i])
    if arr[len(arr)-2] != arr[len(arr)-1]:
        answer.append(arr[len(arr)-1])
    
    return answer