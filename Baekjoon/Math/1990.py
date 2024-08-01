"""
백준 - https://www.acmicpc.net/problem/1990

< 소수인팰린드롬 >
"""

import sys

input = sys.stdin.readline


def is_prime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    p = 5
    while p * p <= x:
        if x % p == 0 or x % (p + 2) == 0:
            return False
        p += 6
    return True


def is_palindrome(x):
    s = str(x)
    if len(s) % 2 == 0 and x != 11:
        return False
    return s == s[::-1]


a, b = map(int, input().split())

for i in range(a, b + 1):
    if is_palindrome(i) and is_prime(i):
        print(i)
print(-1)