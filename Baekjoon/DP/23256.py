"""
백준 - https://www.acmicpc.net/problem/23256

< 성인 게임 >
"""
import sys

input = sys.stdin.readline

# dp[i][0] : 3개만 채워진 상태
# dp[i][1] : 4개 모두 채워진 상태
dp = [[0] * 2 for _ in range(1000000)]

dp[0][0] = 3
dp[0][1] = 4

for i in range(1, 1000000):
    dp[i][0] = (dp[i - 1][0] * 3 + dp[i - 1][1] * 1) % 1000000007
    dp[i][1] = (dp[i - 1][0] * 4 + dp[i - 1][1] * 2) % 1000000007

t = int(input())
for _ in range(t):
    n = int(input())

    print(sum(dp[n - 1]) % 1000000007)
