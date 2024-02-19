"""
백준 - https://www.acmicpc.net/problem/27211

< 도넛 행성 >
"""

import sys

input = sys.stdin.readline
from collections import deque


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if nx == -1:
                nx = n - 1
            if ny == -1:
                ny = m - 1
            if nx == n:
                nx = 0
            if ny == m:
                ny = 0
            
            if not visited[nx][ny] and board[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny))


direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# M칸 오른쪽으로 걸으면 제자리로, N칸 아래로 내려가면 제자리로
# (0, 0)에서 왼쪽은 (0, M - 1), 위로는 (N - 1, 0)
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0 and not visited[i][j]:
            bfs(i, j)
            answer += 1
print(answer)
