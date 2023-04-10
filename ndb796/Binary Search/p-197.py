'''
< 부품 찾기 >
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
    if target > product[middle]:
        return binary_search(target, middle + 1, end)
    else:
        return binary_search(target, start, middle - 1)
    

for i in range(m):
    print(binary_search(order[i], 0, n - 1), end = " ")