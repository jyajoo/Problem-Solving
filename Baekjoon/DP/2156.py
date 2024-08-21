"""
백준 - https://www.acmicpc.net/problem/2156

< 포도주 시식 >
"""

from sys import stdin

input = stdin.readline

n = int(input())
result = 0

# dp[i][2] => i잔까지의 최대 마실 수 있는 양.
# 0 ~ 3까지의 경우의 수
dp = [[0] * 4 for _ in range(n)]

first = int(input())
dp[0][1] = dp[0][3] = first

for i in range(1, n):
    x = int(input())
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + x
    dp[i][2] = max(dp[i - 1][1], dp[i - 1][3])
    dp[i][3] = dp[i - 1][1] + x

print(max(dp[-1]))
