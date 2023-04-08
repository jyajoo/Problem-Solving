'''
< 위에서 아래로 >
'''
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort(key = lambda x : -x)
# arr = sorted(arr, reverse=True)

for i in arr:
    print(i, end = " ")