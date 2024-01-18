"""
백준 - https://www.acmicpc.net/problem/1915

< 가장 큰 정사각형 >
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            val = 0
            if 0 <= i - 1 < n and 0 <= j - 1 < m:
                val = min(board[i - 1][j], board[i - 1][j - 1], board[i][j - 1])

            board[i][j] = val + 1
            answer = max(answer, val + 1)

print(answer**2)
