"""
백준 - https://www.acmicpc.net/problem/2169

< 로봇 조종하기 >
"""

import sys
from copy import deepcopy

input = sys.stdin.readline

n, m = map(int, input().split())

direction = [(0, 1), (0, -1), (0, 1)]

dp = list(map(int, input().split()))
for i in range(1, m):
    dp[i] += dp[i - 1]

for i in range(1, n):
    board = list(map(int, input().split()))

    # 왼쪽 누적합
    left = [0] * m
    left[0] = dp[0] + board[0]
    for j in range(1, m):
        left[j] = max(left[j - 1], dp[j]) + board[j]

    # 오른쪽 누적합
    right = [0] * m
    right[-1] = dp[-1] + board[-1]
    for j in range(m - 2, -1, -1):
        right[j] = max(right[j + 1], dp[j]) + board[j]

    for j in range(m):
        dp[j] = max(left[j], right[j])

print(dp[-1])
