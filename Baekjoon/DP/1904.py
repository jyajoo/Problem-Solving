"""
백준 - https://www.acmicpc.net/problem/1904

< 01타일 >
"""
import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)

mod = 15746
result = 0

if n <= 3:
    result = n

else:
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    for i in range(4, n + 1):
        dp[i] = (dp[i - 2] + dp[i - 1]) % mod

    result = dp[n]

print(result)
"""
"""
import sys

input = sys.stdin.readline

n = int(input())
mod = 15746

a, b = 1, 1
for i in range(2, n + 1):
    result = (a + b) % mod
    a, b = b, result

if n == 1:
    result = 1
print(result)
