"""
백준 - https://www.acmicpc.net/problem/7576

< 토마토 >
"""
import sys
from collections import deque


def check_all(tomato):
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 0:
                return False
    return True


input = sys.stdin.readline

m, n = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(n)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 0 - 안익음, 1 - 익음, -1 - 없음
result = -1
good = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            good.append((0, i, j))

while good:
    d, x, y = good.popleft()

    for dx, dy in direction:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if tomato[nx][ny] == 0:
            tomato[nx][ny] = 1
            good.append((d + 1, nx, ny))

if check_all(tomato):
    result = d
else:
    result = -1
print(result)

'''
'''
import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

tomato = (
    [[-1] * (m + 2)]
    + [[-1] + list(map(int, input().split())) + [-1] for _ in range(n)]
    + [[-1] * (m + 2)]
)

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 0 - 안익음, 1 - 익음, -1 - 없음
cnt = 0
good = deque()
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if tomato[i][j] == 1:
            good.append((0, i, j))
        elif tomato[i][j] == 0:
            cnt += 1

while good:
    d, x, y = good.popleft()

    for dx, dy in direction:
        nx = x + dx
        ny = y + dy
        if tomato[nx][ny] == 0:
            cnt -= 1
            tomato[nx][ny] = 1
            good.append((d + 1, nx, ny))

if cnt == 0:
    print(d)
else:
    print(-1)
