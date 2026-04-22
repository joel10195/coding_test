def solution(arr1, arr2):
    arr = []
    in_arr = []
    row = len(arr1)
    column = len(arr1[0])
    for i in range(row):
        for j in range(column):
            in_arr.append(arr1[i][j] + arr2[i][j])
        arr.append(in_arr)
        in_arr = []
    return arr