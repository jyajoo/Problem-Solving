'''
백준 - https://www.acmicpc.net/problem/2583

< 영역 구하기 >
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    global visited
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    count = 1
    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if nx >= 0 and nx < m and ny >= 0 and ny < n and not visited[nx][ny] and not board[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                count += 1
    return count


m, n, k = map(int, input().split())
board = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for y in range(y1, y2):
        for x in range(x1, x2):
            board[m - y - 1][x] = 1

visited = [[False] * n for _ in range(m)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = []
for i in range(m):
    for j in range(n):
        if not board[i][j] and not visited[i][j]:
            answer.append(bfs(i, j))
answer.sort()
print(len(answer))
print(*answer, sep = ' ')