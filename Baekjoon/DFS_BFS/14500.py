"""
백준 - https://www.acmicpc.net/problem/14500

< 테트로미노 > 
"""

import sys


def dfs(step, score, x, y):
    global answer, visited

    if step == 4:
        answer = max(answer, score)
        return

    for dx, dy in direction:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(step + 1, score + board[nx][ny], nx, ny)
            visited[nx][ny] = False


def find(x, y):
    global answer
    blocks = []
    for dx, dy in direction:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        blocks.append(board[nx][ny])

    if len(blocks) == 4:
        answer = max(answer, board[x][y] + sum(blocks) - min(blocks))
    elif len(blocks) == 3:
        answer = max(answer, board[x][y] + sum(blocks))


input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
visited = [[False] * m for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(1, board[i][j], i, j)
        visited[i][j] = False
        find(i, j)
print(answer)
'''
가지치기
가장 큰 수를 연속으로 방문해도 어차피 answer보다 작다면 그대로 return
'''
import sys


def dfs(step, score, x, y):
    global answer, visited

    if score + (4 - step) * max_value <= answer:
        return

    if step == 4:
        answer = max(answer, score)
        return

    for dx, dy in direction:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(step + 1, score + board[nx][ny], nx, ny)
            visited[nx][ny] = False


def find(x, y):
    global answer
    blocks = []
    for dx, dy in direction:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        blocks.append(board[nx][ny])

    if len(blocks) == 4:
        answer = max(answer, board[x][y] + sum(blocks) - min(blocks))
    elif len(blocks) == 3:
        answer = max(answer, board[x][y] + sum(blocks))


input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
max_value = max(max(row) for row in board)
direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
visited = [[False] * m for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(1, board[i][j], i, j)
        visited[i][j] = False
        find(i, j)
print(answer)
