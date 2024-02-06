"""
백준 - https://www.acmicpc.net/problem/11066

< 파일 합치기 >
"""

import sys

input = sys.stdin.readline

# dp[i][j] : i번째부터 j번째까지 합치는데 드는 최소한의 비용
# i부터 j 사이에 m이라는 지점이 있는 경우,
# dp[i][j] = dp[i][m] + dp[m + 1][j] + (i부터 m까지의  합) + (m + 1부터 j까지의 합)

t = int(input())
for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))
    dp = [[0] * k for _ in range(k)]
    sum_val = {-1: 0}
    for idx in range(k):
        sum_val[idx] = sum_val[idx - 1] + files[idx]

    for size in range(1, k):
        for start in range(k - 1):
            end = start + size
            if end >= k:
                break
            result = int(1e9)
            for middle in range(start, end):
                result = min(
                    result,
                    dp[start][middle]
                    + dp[middle + 1][end]
                    + sum_val[end]
                    - sum_val[start - 1],
                )
            dp[start][end] = result
    print(dp[0][-1])
