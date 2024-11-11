"""
백준 - https://www.acmicpc.net/problem/7562

< 나이트의 이동 >
"""

import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    q = deque()
    visited = [[False] * l for _ in range(l)]
    x, y = start
    q.append((x, y, 0))
    a, b = end
    visited[x][y] = True
    direction = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
    while q:
        x, y, c = q.popleft()
        if x == a and y == b:
            return c

        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if nx >= 0 and nx < l and ny >= 0 and ny < l and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, c + 1))


t = int(input())
for _ in range(t):
    l = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    print(bfs())
