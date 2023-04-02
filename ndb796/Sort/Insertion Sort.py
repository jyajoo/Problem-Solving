'''
< 삽입 정렬 >
'''

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
    idx = i
    for j in range(i, -1, -1):
        if arr[i] < arr[j]:
            idx = j
    val = arr[i]
    arr[idx + 1 : i + 1] = arr[idx : i]
    arr[idx] = val
            
print(arr)
