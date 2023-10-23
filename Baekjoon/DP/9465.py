"""
백준 - https://www.acmicpc.net/problem/9465

< 스티커 >
"""
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]

    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue

    dp[0][1] = dp[1][0] + sticker[0][1]
    dp[1][1] = dp[0][0] + sticker[1][1]
    if n == 2:
        print(max(dp[0][1], dp[1][1]))
        continue

    for i in range(2, n):
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + sticker[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + sticker[1][i]

    print(max(dp[0][-1], dp[1][-1]))
'''
'''
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]

    for i in range(1, n):
        if i > 1:
            dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + dp[0][i]
            dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + dp[1][i]
        else:
            dp[0][i] += dp[1][i - 1]
            dp[1][i] += dp[0][i - 1]

    print(max(dp[0][-1], dp[1][-1]))