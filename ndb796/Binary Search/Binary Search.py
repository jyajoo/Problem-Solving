'''
< 이진 탐색 >
'''
def binary_search(start, end, arr, target):
    if start > end:
        return None
    
    middle = (end + start) // 2
    if target == arr[middle]:
        return middle + 1
    if target < arr[middle]:
        end = middle - 1
    elif target > arr[middle]:
        start = middle + 1

    return binary_search(start, end, arr, target)

n, target = map(int, input().split())
arr = list(map(int, input().split()))

result = binary_search(0, n - 1, arr, target)
print(result)