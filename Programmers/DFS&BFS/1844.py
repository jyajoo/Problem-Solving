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

'''
'''
from collections import deque

def solution(maps):
    answer = int(1e9)
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    n, m = len(maps), len(maps[0])
    
    def bfs(x, y):
        nonlocal answer
        visited = [[False] * m for _ in range(n)]
        q = deque()
        q.append((x, y, 1))
        visited[x][y] = True
        while q:
            x, y, count = q.popleft()
            
            if x == n - 1 and y == m - 1:
                answer = min(answer, count)
                return 
            
            for dx, dy in direction:
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, count + 1))
        
    bfs(0, 0)
    if answer == int(1e9):
        return -1
    return answer