"""
백준 - https://www.acmicpc.net/problem/20542

< 받아쓰기 >
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
start = list(input().strip())
end = list(input().strip())

board = [[int(139)] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1):
    board[i][0] = i

for j in range(m + 1):
    board[0][j] = j

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if (
            (start[i - 1] == end[j - 1])
            or (end[j - 1] in ["i", "j", "l"] and start[i - 1] == "i")
            or (end[j - 1] in ["v", "w"] and start[i - 1] == "v")
        ):
            board[i][j] = board[i - 1][j - 1]

        else:
            board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1

print(board[-1][-1])
