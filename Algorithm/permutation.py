'''
순열 구현
'''

def permutations(arr, n):
    result = []
    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        p = arr[i]
        for j in permutations(arr[:i] + arr[i + 1:], n - 1):
            result.append([p] + j)
    return result
    

arr = [0, 1, 2]
print(permutations(arr, 3))