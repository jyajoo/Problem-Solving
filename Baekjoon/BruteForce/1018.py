"""
백준 - https://www.acmicpc.net/problem/1018

< 체스판 다시 칠하기 >
"""
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(input().rstrip()))

answer = int(1e9)

x = y = 0

while True:
    count = count2 = 0
    p = board[x][y]
    for i in range(x, x + 8):
        for j in range(y, y + 8):
            if i % 2 == 0:
                if j % 2 == 0:
                    if board[i][j] != p:
                        count += 1
                    else:
                        count2 += 1
                else:
                    if board[i][j] == p:
                        count += 1
                    else:
                        count2 += 1
            else:
                if j % 2 == 0:
                    if board[i][j] == p:
                        count += 1
                    else:
                        count2 += 1
                else:
                    if board[i][j] != p:
                        count += 1
                    else:
                        count2 += 1
    answer = min(answer, count, count2)
    y += 1

    if y + 8 > m:
        y = 0
        x += 1

        if x + 8 > n:
            break

print(answer)