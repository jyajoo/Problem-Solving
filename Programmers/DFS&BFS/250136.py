"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/250136

< 석유 시추 >
"""

from collections import deque

land = []
visited = []


def bfs(i, j, num):
    global land, visited, n, m

    q = deque()
    q.append((i, j))
    count = 1
    visited[i][j] = num
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if land[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = num
                count += 1
                q.append((nx, ny))
    return count


def solution(l):
    global land, visited, n, m
    land = l
    result = 0
    n, m = len(l), len(l[0])
    visited = [[0] * m for _ in range(n)]
    size = [0]
    num = 1
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == 0:
                size.append(bfs(i, j, num))
                num += 1

    for j in range(m):
        count = 0
        nums = []
        for i in range(n):
            if land[i][j] == 1:
                num = visited[i][j]
                if num not in nums:
                    nums.append(num)
                    count += size[num]
        result = max(result, count)
    return result
