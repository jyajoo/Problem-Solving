"""
백준 - https://www.acmicpc.net/problem/15724

< 주지수 >
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) + [0] for _ in range(n)]
k = int(input())

dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = board[i - 1][j - 1]
        dp[i][j] += dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    total = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    print(total)
