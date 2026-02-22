'''
백준 - https://www.acmicpc.net/problem/11727

< 2xn 타일링 2 >
'''
'''
다이나믹 프로그래밍
dp[n] = dp[n - 1] + dp[n - 2] * 2
'''
import sys

input = sys.stdin.readline

n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 10007
    print(dp[n])