"""
백준 - https://www.acmicpc.net/problem/12865

< 평범한 배낭 >
"""
import sys

input = sys.stdin.readline

# 개수, 무게
n, k = map(int, input().split())
item = []
for _ in range(n):
    # 무게, 가치
    w, v = map(int, input().split())
    item.append((w, v))

item.sort(key=lambda x: -x[1])

dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w, v = item[i - 1]

        if w > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], v + dp[i - 1][j - w])

print(dp[n][k])