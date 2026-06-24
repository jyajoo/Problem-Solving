'''
백준 - https://www.acmicpc.net/problem/16948

< 데스 나이트 >
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b):
    global answer
    q = deque()
    visited = [[False] * n for _ in range(n)]
    visited[a][b] = True
    q.append((a, b, 0))

    while q:
        x, y, dist = q.popleft()

        if x == r2 and y == c2:
            answer = dist

        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if nx >= 0 and nx < n and ny >= 0 and ny < n and not visited[nx][ny]:
                q.append((nx, ny, dist + 1))
                visited[nx][ny] = True


direction = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
answer = -1
bfs(r1, c1)
print(answer)