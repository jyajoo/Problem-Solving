'''
백준 - https://www.acmicpc.net/problem/3896

< 소수 사이 수열 >
'''
import sys
from bisect import bisect_left

input = sys.stdin.readline

def is_prime(n):
    if n == 1:
        return False
    if n <= 3:
        return True
    
    for i in range(2, int(n ** (1/2)) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    a, b = n, n
    while True:
        if is_prime(a):
            break
        a -= 1

    while True:
        if is_prime(b):
            break
        b += 1

    if a > b or a == n or b == n:
        print(0)
    else:
        print(b - a)