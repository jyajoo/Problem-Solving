"""
백준 - https://www.acmicpc.net/problem/18428

< 감시 피하기 >
"""
import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
board = [list(input().split()) for _ in range(n)]

x = []
teachers = []
for i in range(n):
    for j in range(n):
        if board[i][j] == "X":
            x.append((i, j))
        elif board[i][j] == "T":
            teachers.append((i, j))


def findStudent(x, y):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for x, y in teachers:
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            while nx >= 0 and nx < n and ny >= 0 and ny < n:
                if board[nx][ny] == "S":
                    return True
                elif board[nx][ny] == "O":
                    break
                nx += dx
                ny += dy
    return False


result = False
for data in combinations(x, 3):
    for x, y in data:
        board[x][y] = "O"

        if not findStudent(x, y):
            result = True
            break
    for x, y in data:
        board[x][y] = "X"
if result:
    print("YES")
else:
    print("NO")
