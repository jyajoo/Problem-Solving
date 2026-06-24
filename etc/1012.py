'''
백준 - https://www.acmicpc.net/problem/1012

< 유기농 배추 >
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    global visited
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    while q:
        x, y = q.popleft()

        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if nx >= 0 and nx < n and ny >= 0 and ny < m and not visited[nx][ny] and board[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[False] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for _ in range(k):
        a, b = map(int, input().split())
        board[b][a] = True

    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] and not visited[i][j]:
                bfs(i, j)
                answer += 1

    print(answer)