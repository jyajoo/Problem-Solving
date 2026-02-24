'''
백준 - https://www.acmicpc.net/problem/10844

< 쉬운 계단 수 >
'''
import sys

input = sys.stdin.readline

n = int(input())
dp = [1] * 10

if n == 1:
    print(9)
else:
    for i in range(2, n + 1):
        new = [0] * 10
        for j in range(10):
            if i == 2 and j == 0:
                continue

            if j == 0:
                new[j + 1] += dp[j]
            elif j == 9:
                new[j - 1] += dp[j]
            else:
                new[j - 1] += dp[j]
                new[j + 1] += dp[j]
        dp = new
    print(sum(dp) % 1000000000)