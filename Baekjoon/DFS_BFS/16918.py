"""
백준 - https://www.acmicpc.net/problem/16918

< 봄버맨 >

- 폭발 효과를 한 번에 적용할 수 있도록 해보자
- 폭탄의 설치할 때와, 폭발할 때를 각각 저장해서 관리해보자
"""

import sys
from collections import deque


def install(time):
    for i in range(r):
        for j in range(c):
            if board[i][j] == ".":
                board[i][j] = "O"
                bomb.append((time, i, j))


input = sys.stdin.readline

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
r, c, n = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]

time = 0
bomb = deque()
for i in range(r):
    for j in range(c):
        if board[i][j] == "O":
            bomb.append((time, i, j))

while time <= n:
    if time % 2 == 0 and time != 0:  # 폭탄 설치
        install(time)

    elif time % 2 == 1 and time != 1:  # 폭탄 폭발
        size = len(bomb)
        for _ in range(size):
            start_time, x, y = bomb.popleft()
            if time - start_time == 3:  # 폭발
                board[x][y] = "."
                for dx, dy in direction:
                    nx = x + dx
                    ny = y + dy

                    if nx < 0 or nx >= r or ny < 0 or ny >= c:
                        continue
                    board[nx][ny] = "."

            else:
                if board[x][y] == "O":
                    bomb.append((start_time, x, y))

    time += 1
for i in board:
    print("".join(i))
