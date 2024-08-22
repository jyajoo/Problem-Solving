"""
백준 - https://www.acmicpc.net/problem/15989

< 1, 2, 3 더하기 4 >
"""
from sys import stdin

input = stdin.readline
t = int(input())

dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i - 2]

for i in range(3, 10001):
    dp[i] += dp[i - 3]

for _ in range(t):
    n = int(input())
    print(dp[n])
'''
'''
from sys import stdin

input = stdin.readline

# dp[i][3] 
# i일 때, 이전 수에서 각각 1, 2, 3을 더하는 경우의 수
dp = [[0] * 3 for _ in range(10001)]

dp[1][0] = 1
dp[2][0] = 1
dp[2][1] = 1
dp[3][0] = 1
dp[3][1] = 1
dp[3][2] = 1

for i in range(4, 10001):
    dp[i][0] = dp[i - 1][0]
    dp[i][1] = dp[i - 2][0] + dp[i - 2][1]
    dp[i][2] = dp[i - 3][0] + dp[i - 3][1] + dp[i - 3][2]

t = int(input())
for _ in range(t):
    n = int(input())
    print(sum(dp[n]))
