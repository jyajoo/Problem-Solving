"""
백준 - https://www.acmicpc.net/problem/1004

< 어린 왕자 >
"""

import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())

    answer = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())

        d = abs(x1 - cx) ** 2 + abs(y1 - cy) ** 2
        d2 = abs(x2 - cx) ** 2 + abs(y2 - cy) ** 2

        if d <= r**2 or d2 <= r**2:
            answer += 1
        if d <= r**2 and d2 <= r**2:
            answer -= 1
    print(answer)
