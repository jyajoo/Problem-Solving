"""
백준 - https://www.acmicpc.net/problem/16236

< 아기 상어 >
"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


# 물고기 먹으러 최단 거리로 이동하기
def bfs(shark_pos, fish_pos):
    q = deque()
    visited = [[False] * n for _ in range(n)]
    x, y = shark_pos
    q.append((x, y, 0))
    visited[x][y] = True
    a, b = fish_pos
    while q:
        x, y, dist = q.popleft()
        if x == a and y == b:
            return dist

        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            # 물고기의 크기가 아기 상어보다 작거나 같은지
            # 방문한 적이 있는지를 확인한다.
            if (
                0 <= nx < n
                and 0 <= ny < n
                and board[nx][ny] <= shark_size
                and not visited[nx][ny]
            ):
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))

    return int(1e9)


direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
shark_size = 2  # 상어 크기

# 상어 위치 찾기
# 먹을 수 있는 물고기 찾기
shark_pos = ()
fishes = []
for i in range(n):
    for j in range(n):
        # 아기 상어의 위치 파악
        if board[i][j] == 9:
            shark_pos = (i, j)
            board[i][j] = 0

        # 아기 상어의 크기보다 작은 위치 파악
        if 0 < board[i][j] < shark_size:
            fishes.append((i, j))

result = 0
count = 0
while True:
    if count == shark_size:
        count = 0
        shark_size += 1

    fishes = []
    for i in range(n):
        for j in range(n):
            # 아기 상어의 크기보다 작은 위치 파악
            if 0 < board[i][j] < shark_size:
                fishes.append((i, j))

    # 더 이상 먹을 수 있는 물고기가 없다면, 종료
    if len(fishes) == 0:
        print(result)
        break

    # 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
    elif len(fishes) == 1:
        x, y = fishes[0]
        # 현재의 상어 위치를 목표로 하는 물고기 위치로 최단 거리 이동
        dist = bfs(shark_pos, (x, y))
        fishes.remove((x, y))

        if dist != int(1e9):
            # 현재 상어 위치 반영
            # 거리 반영
            # 상어의 크기 반영
            # 빈 칸으로 반영
            shark_pos = (x, y)
            result += dist
            count += 1
            board[x][y] = 0
        else:
            print(result)
            break

    # 먹을 수 있는 물고기가 1마리 이상이라면, 거리가 최소이고, 가장 위(x가 가장 작음), 가장 왼쪽(y가 가장 작음)인 물고기를 목표로 한다
    else:
        min_dist = int(1e9)
        x, y = int(1e9), int(1e9)
        for i, j in fishes:
            dist = bfs(shark_pos, (i, j))
            if dist < min_dist:
                min_dist = dist
                x, y = i, j
            if dist == min_dist:
                if i < x:
                    x, y = i, j
                    continue
                if i == x:
                    if j < y:
                        x, y = i, j

        fishes.remove((x, y))
        if min_dist != int(1e9):
            shark_pos = (x, y)
            result += min_dist
            count += 1
            board[x][y] = 0
        else:
            print(result)
            break
