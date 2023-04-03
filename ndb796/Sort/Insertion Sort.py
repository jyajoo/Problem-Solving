'''
< 삽입 정렬 >

- 5, 7, 9, 0에서 0이 어디로 들어가야할지 위치를 알아낸다.
- 기존 수들을 오른쪽으로 한칸씩 미뤄 넣는다
- _ , 5, 7, 9 상태가 됨
- 0을 넣어야하는 위치에 넣어주어 0, 5, 7, 9로 만듬
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

'''
- 5, 7, 9, 0에서 왼쪽으로 차례대로 수를 비교해나가며 위치 스와핑
- 5, 7, 0, 9
- 5, 0, 7, 9
- 0, 5, 7, 9 가 된다.
'''
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
        else:
            break
print(arr)