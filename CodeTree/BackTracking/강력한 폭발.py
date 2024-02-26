"""
코드 트리 - https://www.codetree.ai/missions/2/problems/strong-explosion?&utm_source=clipboard&utm_medium=text

< 강력한 폭발 >
"""
# 폭탄 종류에 대해 가능한 모든 순열을 만들어라
# 폭탄 종류는 3개, n만큼 중복 순열 만들기
from itertools import product

directions = [
    [(-2, 0), (-1, 0), (1, 0), (2, 0)],
    [(-1, 0), (1, 0), (0, -1), (0, 1)],
    [(-1, -1), (-1, 1), (1, -1), (1, 1)],
]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

bombs = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            bombs.append((i, j))

answer = 0
bombs_idxs = [0, 1, 2]
for bombs_lst in product(bombs_idxs, repeat=len(bombs)):
    visited = [[0] * n for _ in range(n)]
    result = len(bombs)
    for i, bomb_idx in enumerate(bombs_lst):
        count = 0
        x, y = bombs[i]
        for dx, dy in directions[bomb_idx]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                if visited[nx][ny] == 0:
                    count += 1
                visited[nx][ny] += 1
        result += count
    answer = max(answer, result)


print(answer)
'''
'''
def dfs(step, count):
    global answer
    global bombs_lst

    if step == len(bombs):
        answer = max(answer, count)
        return

    x, y = bombs[step]
    bombs_lst.add((x, y))

    for direction in directions:
        temp = bombs_lst.copy()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                bombs_lst.add((nx, ny))

        dfs(step + 1, len(bombs_lst))
        bombs_lst = temp  # 다시 되돌리기


directions = [
    [(-2, 0), (-1, 0), (1, 0), (2, 0)],
    [(-1, 0), (1, 0), (0, -1), (0, 1)],
    [(-1, -1), (-1, 1), (1, -1), (1, 1)],
]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

bombs = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            bombs.append((i, j))

bombs_lst = set()
answer = 0
dfs(0, 0)
print(answer)
