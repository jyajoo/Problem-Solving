"""
백준 - https://www.acmicpc.net/problem/9184

< 신나는 함수 실행 >
"""
import sys

input = sys.stdin.readline


def w(a, b, c):
    if dp[a][b][c] != 0:
        return dp[a][b][c]

    if a <= 0 or b <= 0 or c <= 0:
        dp[a][b][c] = 1
        return dp[a][b][c]

    if a < b and b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[a][b][c]

    dp[a][b][c] = (
        w(a - 1, b, c)
        + w(a - 1, b - 1, c)
        + w(a - 1, b, c - 1)
        - w(a - 1, b - 1, c - 1)
    )
    return dp[a][b][c]


dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

for i in range(21):
    for j in range(21):
        for k in range(21):
            w(i, j, k)

while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break

    x, y, z = a, b, c
    if a > 20 or b > 20 or c > 20:
        x, y, z = 20, 20, 20

    if a <= 0 or b <= 0 or c <= 0:
        x, y, z = 0, 0, 0

    result = w(x, y, z)
    print("w({}, {}, {}) = {}".format(a, b, c, result))
