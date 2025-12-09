'''
백준 - https://www.acmicpc.net/problem/1012

< 유기농 배추 >

- 배추들이 모여있는 곳에 배추흰지렁이 한 마리만 필요
- 0은 배추 x, 1은 배추 o

1 <= m, n <= 50 가로세로
1 <= k <= 2500 배추의 개수
시간 복잡도 <= O(N^2)
'''
'''
DFS로 인접한 배추 탐색
시간 복잡도는 O(MN)
'''
import sys

input = sys.stdin.readline

def dfs(x, y):
    global visited
    visited[x][y] = True
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny))

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    result = 0
    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1

    for a in range(n):
        for b in range(m):
            if board[a][b] == 1 and not visited[a][b]:
                dfs(a, b)
                result += 1
    print(result)
'''
DFS로 인접한 배추 탐색(재귀)
'''
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(x, y):
    global visited
    for dx, dy in delta:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny)

t = int(input())
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    result = 0
    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1

    for x in range(n):
        for y in range(m):
            if board[x][y] and not visited[x][y]:
                visited[x][y] = True
                result += 1
                dfs(x, y)
    print(result)
'''
BFS로 인접한 배추 탐색
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    global visited
    q = deque([])
    q.append((x, y))
    visited[x][y] = True
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    result = 0
    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1

    for x in range(n):
        for y in range(m):
            if board[x][y] and not visited[x][y]:
                bfs(x, y)
                result += 1

    print(result)