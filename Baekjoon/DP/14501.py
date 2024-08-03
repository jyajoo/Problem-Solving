"""
백준 - https://www.acmicpc.net/problem/14501

< 퇴사 >
"""
import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1)
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n - 1, -1, -1):
    t, p = arr[i]

    if i + t <= n:
        dp[i] = max(dp[i + 1], p + dp[i + t])
    else:
        dp[i] = dp[i + 1]
print(dp[0])
