"""
백준 - https://www.acmicpc.net/problem/14658

< 하늘에서 별똥별이 빗발친다 >
"""

from sys import stdin

input = stdin.readline

n, m, l, k = map(int, input().split())

stars = []
for _ in range(k):
    x, y = map(int, input().split())
    stars.append((x, y))

max_val = 0
for a1, b1 in stars:
    for a2, b2 in stars:
        a, b = min(a1, a2), min(b1, b2)
        count = 0
        for x, y in stars:
            if a <= x <= a + l and b <= y <= b + l:
                count += 1
        max_val = max(max_val, count)

print(k - max_val)
