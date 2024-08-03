"""
백준 - https://www.acmicpc.net/problem/2847

< 게임을 만든 동준이 >
"""

import sys

input = sys.stdin.readline

n = int(input())
num = [int(input()) for _ in range(n)]

result = 0
score = num[-1] - 1
for i in range(n - 2, -1, -1):
    if num[i] < score:
        score = num[i]

    result += num[i] - score
    score -= 1

    if score < 1:
        score = 1
print(result)
