"""
백준 - https://www.acmicpc.net/problem/1890

< 점프 >

"""
import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]

dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n -1 and j == n - 1:
            break
        cnt = arr[i][j]

        if i + cnt < n:
            dp[i + cnt][j] += dp[i][j]
        
        if j + cnt < n:
            dp[i][j + cnt] += dp[i][j]

print(dp[n - 1][n - 1])