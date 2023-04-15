'''
< 1로 만들기 >
'''
n = int(input())
result = 0
def one(n):
    global result
    if n == 1:
        return result
    result += 1
    if n % 5 == 0:
        return one(n / 5)
    elif n % 3 == 0:
        return one(n / 3)
    elif (n - 1) % 5 == 0 or (n - 1) % 3 == 0:
        return one(n - 1)
    elif n % 2 == 0:
        return one(n / 2)
    else:
        return one(n - 1)

print(one(n))

'''
- 메모이제이션 적용
- 바텀업 방식 사용
'''
n = int(input())
d = [0] * 30001

for i in range(2, n + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    elif i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    elif i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
    
print(d[n])