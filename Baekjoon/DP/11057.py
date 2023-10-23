'''
백준 - https://www.acmicpc.net/problem/11057

< 오르막 수 >
'''
import sys

input = sys.stdin.readline

n = int(input())
dp = [1] * 10

for i in range(n - 1):
    for j in range(1, 10):
        dp[j] += dp[j - 1]

print(sum(dp) % 10007)

'''
'''
import sys

input = sys.stdin.readline

n = int(input())
dp = [[0] * 10 for _ in range(n + 1)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(sum(dp[n]) % 10007)