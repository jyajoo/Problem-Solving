'''
백준 - https://www.acmicpc.net/problem/1149

< RGB거리 >
'''
from sys import stdin

input = stdin.readline

n = int(input())

answer = int(1e9)
# dp[n][3] : n번째 집에서 (0, 1, 2) 색상을 칠할 때 드는 최소비용
dp = [[0] * 3 for _ in range(n)]

for i in range(n):
    a, b, c = map(int, input().split())
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + a
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + b
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + c

print(min(dp[-1]))
