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
'''
