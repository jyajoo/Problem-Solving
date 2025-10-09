'''
백준 - https://www.acmicpc.net/problem/10026

< 적록색약 >

- 적록색약인 사람과 아닌 사람이 보는 구역의 수
1 <= n <= 100
시간 복잡도 <= O(N^3)
'''
'''
DFS(비재귀)
'''
import sys
input = sys.stdin.readline

def dfs(x, y, k, is_color_blind, visited):
    stack = []
    stack.append((x, y))
    visited[x][y] = True
    while stack:
        x, y = stack.pop()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if (not is_color_blind or (is_color_blind and k == 'B'))and board[nx][ny] == k:
                    visited[nx][ny] = True
                    stack.append((nx, ny))

                elif is_color_blind and (k != 'B') and (board[nx][ny] != 'B'):
                    visited[nx][ny] = True
                    stack.append((nx, ny))

n = int(input())
board = []
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(n):
    board.append(list(input().strip()))

visited = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]
count = count2 = 0
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            dfs(x, y, board[x][y], False, visited)
            count += 1
        if not visited2[x][y]:
            dfs(x, y, board[x][y], True, visited2)
            count2 += 1

print(count, count2)
'''
복잡한 조건문 제거, Board 단순화
'''
import sys
input = sys.stdin.readline

def dfs(x, y, k, board, visited):
    stack = []
    stack.append((x, y))
    visited[x][y] = True
    while stack:
        x, y = stack.pop()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == k and not visited[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny))

n = int(input())
board = []
new_board = []

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(n):
    a = input().strip()
    board.append(list(a))
    new_board.append(list(a.replace('G', 'R')))

visited = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]
count = count2 = 0
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            dfs(x, y, board[x][y], board, visited)
            count += 1

        if not visited2[x][y]:
            dfs(x, y, new_board[x][y], new_board, visited2)
            count2 += 1

print(count, count2)