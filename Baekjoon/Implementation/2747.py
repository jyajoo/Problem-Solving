'''
백준 - https://www.acmicpc.net/problem/2747

< 피보나치 수 >

- 0과 1에 대한 예외 처리를 하지 않으면 런타임 에러.
'''
# n = int(input())

# arr = [0] * (n + 1)     # 수의 시작은 0부터이다.
# arr[0] = 0
# arr[1] = 1

# for i in range(2, n + 1):
#     arr[i] = arr[i - 1] + arr[i - 2]

# print(arr[n])

'''
- 0과 1에 대한 예외 처리 추가
'''

def fibo(n):
    if n == 0 or n == 1:
        return n

    arr = [0] * (n + 1) 
    arr[0] = 0
    arr[1] = 1

    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr[n]

n = int(input())

print(fibo(n))

'''
- 배열 공간 두 가지 수만 들어가도 된다.
'''

def fibo(n):
    arr = [0, 1]

    if n == 0 or n == 1:
        return n

    for i in range(2, n + 1):
        # answer = arr[0] + arr[1]
        answer = sum(arr)
        arr = [arr[1], answer]

    return answer


n = int(input())

print(fibo(n))

'''
- 배열을 이용하지 않고 변수 swwap 이용하기
'''

n = int(input())

a, b = 0, 1

for i in range(n):
    a, b = b, a + b

print(a)
