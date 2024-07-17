"""
백준 - https://www.acmicpc.net/problem/21317

< 징검다리 건너기 >
"""

import sys

input = sys.stdin.readline

n = int(input())
dp = [[int(1e9)] * 2 for _ in range(n + 1)]

jumps = [()]
for _ in range(n - 1):
    a, b = map(int, input().split())
    jumps.append((a, b))

k = int(input())
dp[1][0] = 0
dp[1][1] = 0
for i in range(1, n + 1):
    # 작은 점프
    if i + 1 <= n:
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + jumps[i][0])
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][1] + jumps[i][0])

    # 큰 점프
    if i + 2 <= n:
        dp[i + 2][0] = min(dp[i + 2][0], dp[i][0] + jumps[i][1])
        dp[i + 2][1] = min(dp[i + 2][1], dp[i][1] + jumps[i][1])

    if i + 3 <= n:
        # 매우 큰 점프
        dp[i + 3][1] = min(dp[i + 3][1], dp[i][0] + k)

print(min(dp[-1]))
