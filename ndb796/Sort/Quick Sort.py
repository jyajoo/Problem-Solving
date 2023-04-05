'''
< 퀵 정렬 >
'''
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick(arr, start, end):
    if end - start < 1:
        return
    pivot = arr[start]
    i, j = 0, 0
    while True:
        for x in range(start + 1, end + 1):
            if pivot < arr[x]:
                i = x
                break
        for x in range(end, start, -1):
            if pivot > arr[x]:
                j = x
                break
        if i != 0 and j != 0:
            if i > j:
                arr[start], arr[j] = arr[j], arr[start]
                break
            arr[i], arr[j] = arr[j], arr[i]
        elif i == 0:
            arr[start:end] = arr[start+1:end+1]
            arr[end] = pivot
            j = end - 1
            break
        elif j == 0:
            j = start
            break
    quick(arr, start, j)
    quick(arr, j + 1, end)

quick(arr, 0, len(arr) - 1)
print(arr)
