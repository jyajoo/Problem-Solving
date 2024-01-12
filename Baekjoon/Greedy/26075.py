"""
백준 - https://www.acmicpc.net/problem/26075

< 곰곰아 선 넘지마 >
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
s = input().strip()
t = input().strip()
num = "0"
if n > m:
    num = "1"

num_s = []
num_t = []

for i in range(len(s)):
    if s[i] == num:
        num_s.append(i)

    if t[i] == num:
        num_t.append(i)

x = y = 0
index = 0

for i in range(len(num_s)):
    diff = abs(num_s[i] - num_t[i])
    if diff % 2 == 0:
        x += diff // 2
        y += diff // 2
    else:
        if x < y:
            x += diff // 2 + 1
            y += diff // 2
        else:
            x += diff // 2
            y += diff // 2 + 1


print(x**2 + y**2)
