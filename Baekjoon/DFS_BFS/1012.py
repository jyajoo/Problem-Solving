'''
백준 - https://www.acmicpc.net/problem/1012

< 유기농 배추 >

- 배추들이 모여있는 곳에 배추흰지렁이 한 마리만 필요
- 0은 배추 x, 1은 배추 o

1 <= m, n <= 50 가로세로
1 <= k <= 2500 배추의 개수

'''
'''
DFS로 인접한 배추 탐색
시간복잡도는 O(N^2)
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