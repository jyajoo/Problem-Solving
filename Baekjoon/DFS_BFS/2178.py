"""
백준 - https://www.acmicpc.net/problem/2178

< 미로 탐색 >
"""

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = (
    [[0] * (m + 2)]
    + [[0] + list(map(int, list(input().strip()))) + [0] for _ in range(n)]
    + [[0] * (m + 2)]
)
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = (
    [[True] * (m + 2)]
    + [[True] + [False] * m + [True] for _ in range(n)]
    + [[True] * (m + 2)]
)
q = deque()
q.append((1, 1, 1))
visited[1][1] = True
result = int(1e9)

while q:
    cnt, x, y = q.popleft()

    if x == n and y == m:
        result = min(result, cnt)
        break

    for dx, dy in direction:
        nx = x + dx
        ny = y + dy
        if board[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((cnt + 1, nx, ny))

print(result)

"""
"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, list(input().strip()))) for _ in range(n)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * m for _ in range(n)]
q = deque()
q.append((1, 0, 0))
visited[0][0] = True
result = int(1e9)

while q:
    cnt, x, y = q.popleft()

    if x == n - 1 and y == m - 1:
        result = min(result, cnt)
        break

    for dx, dy in direction:
        nx = x + dx
        ny = y + dy

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if board[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((cnt + 1, nx, ny))

print(result)
'''
'''
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, list(input().strip()))) for _ in range(n)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * m for _ in range(n)]
q = deque()
q.append((1, 0, 0))
visited[0][0] = True

while q:
    cnt, x, y = q.popleft()

    for dx, dy in direction:
        nx = x + dx
        ny = y + dy

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if board[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((cnt + 1, nx, ny))
            board[nx][ny] = cnt + 1

print(board[-1][-1])