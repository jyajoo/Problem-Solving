"""
백준 - https://www.acmicpc.net/problem/12852

<1로 만들기 2>
"""
import sys

input = sys.stdin.readline
n = int(input())
dp = [[i] for i in range(n + 1)]
dp[1] = [1]
for i in range(2, n + 1):
    if i % 3 == 0:
        dp[i] = [i] + dp[i // 3]

    if i % 2 == 0:
        if len(dp[i]) == 1 or len(dp[i]) > len(dp[i // 2]) + 1:
            dp[i] = [i] + dp[i // 2]

    if len(dp[i]) == 1 or len(dp[i]) > len(dp[i - 1]) + 1:
        dp[i] = [i] + dp[i - 1]

print(len(dp[n]) - 1)
print(*dp[n])

"""
"""
import sys

input = sys.stdin.readline
n = int(input())
dp = [0] * (n + 1)
path = [[i] for i in range(n + 1)]

path[1] = [1]

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    path[i] = [i] + path[i - 1]

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
        path[i] = [i] + path[i // 3]
    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        path[i] = [i] + path[i // 2]

print(dp[n])
print(*path[n])
