"""
백준 - https://www.acmicpc.net/problem/2193

< 이친수 >
"""

import sys

input = sys.stdin.readline

n = int(input())

dp = [[0, 0] for _ in range(n + 1)]

if n <= 2:
    print(1)
else:
    dp[1] = [0, 1]
    dp[2] = [1, 0]
    for i in range(3, n + 1):
        dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
        dp[i][1] = dp[i - 1][0]
    print(sum(dp[-1]))
