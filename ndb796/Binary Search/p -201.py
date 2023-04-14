'''
< 떡볶이 떡 만들기 >

- 부정확한 풀이 (재도전하기)
'''
n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(key = lambda x : x)

result = arr[-1] - m
while True:
    rice = []
    for i in arr:
        if i - result > 0:
            rice.append(i - result)
        else:
            rice.append(0)
    if sum(rice) == m:
        print(result)
        break
    
    for i in rice:
        if i != 0:
            result += i
            break
    print(result)
    break

'''
이진탐색으로 풀이
- 재귀
'''
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(key = lambda x : x)

def binary(start, end, target):
    middle = (start + end) // 2
    rice = 0
    for i in arr:
        if i - middle > 0:
            rice += i - middle
    if rice == target:
        return middle
    elif rice > target:
        return binary(middle + 1, end, target)
    else:
        return binary(start, middle - 1, target)

print(binary(0, arr[-1], m))

'''
이진탐색
- 반복
'''
n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
result = 0
while start <= end:
    middle = (start + end) // 2
    rice = 0
    for i in arr:
        if i - middle > 0:
            rice += i - middle
    if rice < m:
        end = middle - 1
    else:
        result = middle
        start = middle + 1
print(result)