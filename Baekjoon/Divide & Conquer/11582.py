'''
백준 - https://www.acmicpc.net/problem/11582

<치킨 TOP N >
'''
# n = int(input())
# arr = list(map(int, input().split()))
# k = int(input())


# for i in range(k):
#     step = 2 * (i + 1)
#     for i in range(0, len(arr), step):
#         arr[i:i+step] = sorted(arr[i:i+step])

# for i in arr:
#     print(i, end=" ")

####################################################

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

step = n // k
for i in range(0, len(arr), step):
    arr[i:i+step] = sorted(arr[i:i+step])

for i in arr:
    print(i, end=" ")
