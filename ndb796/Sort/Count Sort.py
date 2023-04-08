'''
< 계수 정렬 >
'''
arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

def count(arr):
    max_value = max(arr)
    num = [0] * (max_value + 1)
    
    for i in arr:
        num[i] += 1

    for i in range(len(num)):
        for _ in range(num[i]):
            print(i, end = " ")
count(arr)
