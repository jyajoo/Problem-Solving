"""
백준 - https://www.acmicpc.net/problem/14502
< 연구소 >
"""
import sys
from itertools import combinations
from collections import deque
import copy

input = sys.stdin.readline


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if check[nx][ny] == 0:
                    check[nx][ny] = 2
                    queue.append((nx, ny))


n, m = map(int, input().split())
research = [list(map(int, input().split())) for _ in range(n)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
wall = []
virus = []
for i in range(n):
    for j in range(m):
        # 벽을 세울 수 있는 칸이라면,
        if research[i][j] == 0:
            wall.append((i, j))
        # 바이러스
        elif research[i][j] == 2:
            virus.append((i, j))

result = 0
for wall in list(combinations(wall, 3)):
    check = copy.deepcopy(research)
    # 벽 세우기
    for x, y in wall:
        check[x][y] = 1

    # 바이러스 bfs 퍼지기
    for x, y in virus:
        bfs(x, y)
    result = max(result, sum(check[i].count(0) for i in range(n)))

print(result)
