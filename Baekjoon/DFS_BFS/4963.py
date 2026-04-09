"""
백준 - https://www.acmicpc.net/problem/4963

< 섬의 개수 >
"""

import sys
from collections import deque

input = sys.stdin.readline


def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if nx >= 0 and nx < h and ny >= 0 and ny < w and board[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


direction = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    board = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] and not visited[i][j]:
                bfs(i, j)
                count += 1
    print(count)
