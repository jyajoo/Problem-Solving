"""
백준 - https://www.acmicpc.net/problem/2168

< 타일 위의 대각선 >
"""

import sys

input = sys.stdin.readline

x, y = map(int, input().split())


# 최대 공약수 구하기
def find_gcd(x, y):
    while x % y != 0:
        r = x % y
        x, y = y, r
    return y


gcd = find_gcd(x, y)

print(x + y - gcd)
