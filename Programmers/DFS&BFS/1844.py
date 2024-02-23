"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/1844

< 게임 맵 최단거리 >
"""

from collections import deque


def bfs(maps, a, b):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((a, b, 1))
    visited[a][b] = True
    while q:
        x, y, cnt = q.popleft()
        if x == n - 1 and y == m - 1:
            return cnt

        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if (
                0 <= nx < n
                and 0 <= ny < m
                and not visited[nx][ny]
                and maps[nx][ny] == 1
            ):
                visited[nx][ny] = True
                q.append((nx, ny, cnt + 1))
    return -1


def solution(maps):
    return bfs(maps, 0, 0)
