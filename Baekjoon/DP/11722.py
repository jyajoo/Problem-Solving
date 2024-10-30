"""
백준 - https://www.acmicpc.net/problem/11722

< 가장 긴 감소하는 부분 수열 >
"""

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        # 현재 숫자보다 작다면,
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
