"""
백준 - https://www.acmicpc.net/problem/11048

< 이동하기 >
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
candy = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]
direction = [(-1, 0), (-1, -1), (0, -1)]
for i in range(n):
    for j in range(m):
        max_candy = 0
        for dx, dy in direction:
            ni = i + dx
            nj = j + dy
            if ni >= 0 and ni < n and nj >= 0 and nj < m:
                max_candy = max(max_candy, dp[ni][nj])
        dp[i][j] = max_candy + candy[i][j]

print(dp[n - 1][m - 1])

"""
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
candy = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = (
            max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + candy[i - 1][j - 1]
        )
print(dp[n][m])
