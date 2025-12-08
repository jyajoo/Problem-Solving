'''
백준 - https://www.acmicpc.net/problem/2468

< 안전 영역 >

- 물에 잠기지 않는 안전 영역이 몇개인지
- 지역의 높이가 n*n 배열 형태로 제공

2 <= n <= 100
1 <= 높이 <= 100
시간 복잡도 <= O(N^2*높이)
'''
'''
BFS로 인접한 안전 영역 탐색
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, h):
    global visited
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > h and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

n = int(input())
board = []
max_h = 0
for _ in range(n):
    arr = list(map(int, input().split()))
    board.append(arr)
    max_h = max(max_h, max(arr))

result = 0
for i in range(max_h + 1):
    count = 0
    visited = [[False] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if board[x][y] > i and not visited[x][y]:
                bfs(x, y, i)
                count += 1
    result = max(result, count)
print(result)
'''
DFS(비재귀)
'''
import sys
input = sys.stdin.readline

def dfs(x, y, h):
    global visited
    stack = []
    stack.append((x, y))
    visited[x][y] = True
    while stack:
        x, y = stack.pop()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > h and not visited[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny))

n = int(input())
board = []
max_h = 0
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(n):
    arr = list(map(int, input().split()))
    board.append(arr)
    max_h = max(max_h, max(arr))

result = 0
for i in range(max_h + 1):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for x in range(n):
        for y in range(n):
            if board[x][y] > i and not visited[x][y]:
                dfs(x, y, i)
                count += 1

    result = max(result, count)
print(result)
'''
DFS(재귀)
'''
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(x, y, i):
    global visited
    stack = []
    stack.append((x, y))
    for dx, dy in direction:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > i and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, i)

n = int(input())
board = []
max_h = 0
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(n):
    arr = list(map(int, input().split()))
    board.append(arr)
    max_h = max(max_h, max(arr))

result = 0
for i in range(max_h + 1):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for x in range(n):
        for y in range(n):
            if board[x][y] > i and not visited[x][y]:
                visited[x][y] = True
                dfs(x, y, i)
                count += 1
    result = max(result, count)
print(result)