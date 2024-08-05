"""
백준 - https://www.acmicpc.net/problem/1669

< 멍멍이 쓰다듬기 >
"""

import sys, math

input = sys.stdin.readline

x, y = map(int, input().split())

result = 0
diff = y - x

n = int(math.sqrt(diff))
if diff <= 2:
    print(diff)
elif n**2 == diff:
    print(n * 2 - 1)
else:
    diff2 = diff - n**2
    if diff2 <= n:
        print(n * 2)
    else:
        print(n * 2 + 1)
'''
'''
from sys import stdin
from math import sqrt

input = stdin.readline

x, y = map(int, input().split())


diff = y - x
n = int(sqrt(diff))

result = 0
if diff == 0:
    result = 0
elif n * n == diff:
    result = n + (n - 1)
else:
    result = n + (n - 1)
    result += (diff - (n * n) - 1) // n + 1


print(result)
