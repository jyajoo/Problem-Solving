'''
백준 - https://www.acmicpc.net/problem/3896

< 소수 사이 수열 >

소수 p, p + n
그 사이에 있는 n-1개의 합성수 = 길이가 n인 소수 사이 수열
양의 정수 k가 주어졌을 때, k를 포함하는 소수 사이 수열의 길이 구하기

1 <= k <= 1299709(100000번째 소수)
'''
'''
K보다 작은 수 중 가장 큰 소수 찾기
K보다 큰 수 중 가장 작은 소수 찾기

'''
import sys
input = sys.stdin.readline

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** (1/2)) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())

    if is_prime(n):
        print(0)
    else:
        for i in range(n - 1, 1, -1):
            if is_prime(i):
                break
        
        for j in range(n, 1299709):
            if is_prime(j):
                break
        print(j - i)
'''
소수 리스트를 구현 후 이진탐색
에라토스테네스의 체
소수인 p의 배수들은 모두 소수가 될 수 없다.
'''
import sys
input = sys.stdin.readline

is_prime = [True] * 1299710
is_prime[0] = is_prime[1] = False
primes = []
for i in range(2, int(1299709 ** (1/2)) + 1):
    if is_prime[i]:
        for j in range(i * i, 1299710, i):
            is_prime[j] = False

for i in range(1, 1299710):
    if is_prime[i]:
        primes.append(i)

t = int(input())
for _ in range(t):
    n = int(input())
    
    if is_prime[n]:
        print(0)
    else: 
        start = 0
        end = len(primes) - 1
        p_idx = -1
        while start <= end:
            middle = (start + end) // 2
            if primes[middle] < n:
                start = middle + 1
                p_idx = middle
            else:
                end = middle - 1
        
        print(primes[p_idx + 1] - primes[p_idx])