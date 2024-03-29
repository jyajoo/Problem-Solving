'''
< 부품 찾기 >
- 이진 탐색(재귀함수)
'''
n = int(input())
product = list(map(int, input().split()))
m = int(input())
order = list(map(int, input().split()))

def binary_search(target, start, end):
    if start > end:
        return 'no'
    middle = (start + end) // 2
    if target == product[middle]:
        return 'yes'
    elif target > product[middle]:
        return binary_search(target, middle + 1, end)
    else:
        return binary_search(target, start, middle - 1)
    

for i in range(m):
    print(binary_search(order[i], 0, n - 1), end = " ")

'''
- 이진탐색(반복문)
'''
def binary_search(arr, target, start, end):
    while start <= end:
        middle = (start + end) // 2
        if target == arr[middle]:
            return 'yes'
        elif target > arr[middle]:
            start = middle + 1
        else:
            end = middle - 1
        
    return None
for i in range(m):
    result = binary_search(product, order[i], 0, n - 1)
    if result == None:
        print("no", end = " ")
    else:
        print(result, end = " ")

'''
- 계수 정렬
'''
# max_value = max(product)
# num = [0 for _ in range(max_value + 1)]
# for i in product:
#     num[i] += 1
num = [0] * 1000001
for i in product:
    num[i] = 1
for i in order:
    if num[i] > 0:
        print("yes", end = " ")
    else:
        print("no", end = " ")

'''
- 집합 자료형 이용
'''
n = int(input())
product = set(map(int, input().split()))
m = int(input())
order = list(map(int, input().split()))

for i in order:
    if i in product:
        print("yes", end = " ")
    else:
        print("no", end = " ")