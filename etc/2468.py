'''
백준 - https://www.acmicpc.net/problem/2468

< 안전 영역 >
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(h, i, j):
    global visited
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx and nx < n and 0 <= ny and ny < n and not visited[nx][ny] and board[nx][ny] - h > 0:
                visited[nx][ny] = True
                queue.append((nx, ny))



n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]

max_h = 0
for i in board:
    for j in i:
        max_h = max(max_h, j)

answer = 0
for h in range(max_h):
    count = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] - h > 0:
                bfs(h, i, j)
                count += 1
    answer = max(answer, count)
print(answer)