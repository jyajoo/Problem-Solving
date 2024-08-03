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
