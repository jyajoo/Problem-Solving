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