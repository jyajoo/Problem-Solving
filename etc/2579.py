'''
백준 - https://www.acmicpc.net/problem/2579

< 계단 오르기 >
'''
'''
dp[n][2]
dp[n][0] : n-1단계 선택 x -> max(dp[i-2]) + arr[n]
dp[n][1] : n-1단계 선택 o -> dp[i-1][0] + arr[n]
'''
import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

if n <= 2:
    print(sum(arr))

else:
    dp = [[0] * 2 for _ in range(n)]
    dp[0] = [arr[0], arr[0]]
    dp[1] = [arr[1], arr[0] + arr[1]]
    for i in range(2, n):
        dp[i][0] = max(dp[i - 2]) + arr[i]
        dp[i][1] = dp[i-1][0] + arr[i]
    print(max(dp[-1]))