'''
< 피보나치 함수 >

- 점화식을 재귀 함수로 표현
'''

'''
시간 복잡도는 O(2^N)이다.
따라서 N이 클 수록, 재귀 함수이기 때문에 메모리에 문제가 발생할 수 있고,
시간도 오래 걸리기 때문에 좋은 방법이 아니다.

'''
def fibo(x):
    if x == 1 or x == 2:
        return 1
    
    return fibo(x-1) + fibo(x-2)


print(fibo(4))

'''
이러한 문제를 해결하기 위해 DP 방식을 이용한다.

메모이제이션이란, 한 번 구한 값은 미리 저장하여 재활용한다. (DP 구현 방식 중 하나)
이 방식을 이용하면 반복적으로 계산할 필요가 없다.
큰 문제에서 작은 문제로 뻗어나가면서 해결하므로 Top-Down, 하향식 방식이라고 한다.
'''

arr = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1

    if arr[x] != 0:
        return arr[x]

    arr[x] = fibo(x - 1) + fibo(x - 2)
    return arr[x]

print(fibo(99))

'''

재귀 함수의 메모리 문제를 방지하고자 반복문을 이용해 해결하기도 한다.
작은 문제부터 해결해 나아가는 Bottom-Up, 상향식 방식이라고 한다.
'''
arr = [0] * 100

arr[1] = 1
arr[2] = 1

for i in range(3, 100):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[99])