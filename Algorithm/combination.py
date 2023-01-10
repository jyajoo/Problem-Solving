'''
< 조합 구현 >
'''
def combinations(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i in range(len(arr)):
        p = arr[i]
        for j in combinations(arr[i + 1:], n - 1):
            result.append([p] + j)

    return result

arr = [0, 1, 2, 3]
print(combinations(arr, 2)) # [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]