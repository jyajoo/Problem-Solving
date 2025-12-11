'''
백준 - https://www.acmicpc.net/problem/3896

< 소수 사이 수열 >

소수 p, p + n
그 사이에 있는 n-1개의 합성수 = 길이가 n인 소수 사이 수열
양의 정수 k가 주어졌을 때, k를 포함하는 소수 사이 수열의 길이 구하기

1 <= k <= 1299709(100000번째 소수)
'''
import sys
input = sys.stdin.readline

def is_decimal(n):
    if n == 1:
        return False
    for i in range(2, int(n ** (1/2)) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())

    if is_decimal(n):
        print(0)
    else:
        for i in range(n - 1, 1, -1):
            if is_decimal(i):
                break
        
        for j in range(n, 1299709):
            if is_decimal(j):
                break
        print(j - i)