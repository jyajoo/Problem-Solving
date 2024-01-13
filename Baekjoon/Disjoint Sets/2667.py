"""
백준 - https://www.acmicpc.net/problem/2667

< 단지 번호 붙이기 >
"""
import sys

input = sys.stdin.readline
from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    count = 1
    board[x][y] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if (
                0 <= nx < n
                and 0 <= ny < n
                and board[nx][ny] == 1
            ):
                board[nx][ny] = 0
                q.append((nx, ny))
                count += 1
    return count


n = int(input())
board = [list(map(int, input().strip())) for _ in range(n)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

result = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            result.append(bfs(i, j))

result.sort(key=lambda x: x)
print(len(result))
for i in result:
    print(i)
"""
"""
import sys

input = sys.stdin.readline


def find_parent(x):
    if type(union[x]) == int and union[x] < 0:
        return x
    else:
        union[x] = find_parent(union[x])
        return union[x]


def find_union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x == y:
        return False
    else:
        union[x] += union[y]
        union[y] = x
        return True


n = int(input())
board = [list(map(int, input().strip())) for _ in range(n)]
union = {}
for i in range(n):
    for j in range(n):
        union[(i, j)] = (i, j)

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            if union[(i, j)] == (i, j):
                union[(i, j)] = -1
            for dx, dy in direction:
                ni = i + dx
                nj = j + dy
                if 0 <= ni < n and 0 <= nj < n and board[ni][nj] == 1:
                    if union[(ni, nj)] == (ni, nj):
                        union[(ni, nj)] = -1
                    find_union((i, j), (ni, nj))

result = []
for i in union.values():
    if type(i) == int:
        result.append(abs(i))

result.sort(key=lambda x: x)
print(len(result))
for i in result:
    print(i)