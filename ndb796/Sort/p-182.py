'''
< 두 배열의 원소 교체 >
'''
n, k = map(int, input().split())
a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

a_arr.sort()
b_arr.sort(key = lambda x : -x)

for i in range(k):
    if a_arr[i] < b_arr[i]:
        a_arr[i], b_arr[i] = b_arr[i], a_arr[i]
    else:
        break

print(sum(a_arr))