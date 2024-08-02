"""
백준 - https://www.acmicpc.net/problem/2234

< 성곽 >
1 (서)
2 (북)
3 (서, 북)
4 (동)
5 (서, 동)
6 (북, 동)
7 (서, 북, 동)
8 (남)
9 (서, 남)
10 (북, 남)
11 (서, 북, 남)
12 (동, 남)
13 (서, 동, 남)
14 (북, 동, 남)
15 (서, 북, 동, 남)

11과 6이 이어져 있는지?
서, 북, 남 -> 동이 없기 때문에, 6에서 서가 없어야 함
북, 동 -> 서가 없음 연결되어있음


11과 7이 이어져 있는지?
서, 북, 남 -> 동이 없기 때문에, 7에서 서가 없어야 함
서, 북, 동 -> 서가 존재. 연결안되어 있음

전제 조건 : 15가 아니고
서(1)가 없는 경우 : 2의 배수
2, 4, 6, 8, 10, 12, 14
동(4)이 없는 경우 : 8로 나눈 나머지가 0, 1, 2, 3인 경우
1, 2, 3, 8, 9, 10, 11
북(2)이 없는 경우 : 4로 나눈 나머지가 0, 1인 경우
1, 4, 5, 8, 9, 12, 13
남(8)이 없는 경우 : 7 이하의 수
1, 2, 3, 4, 5, 6, 7
"""

from sys import stdin
from collections import deque

input = stdin.readline


def bfs(i, j, room_num):
    q = deque()
    q.append((i, j))
    visited[i][j] = room_num
    room_size = 0
    while q:
        x, y = q.popleft()
        direc = []
        room_size += 1

        if board[x][y] == 15:
            continue

        # 북이 없는 경우
        if board[x][y] % 4 < 2:
            direc.append(0)

        # 남이 없는 경우
        if board[x][y] <= 7:
            direc.append(1)

        # 서가 없는 경우
        if board[x][y] % 2 == 0:
            direc.append(2)

        # 동이 없는 경우
        if board[x][y] % 8 < 4:
            direc.append(3)

        for d in direc:
            nx = x + direction[d][0]
            ny = y + direction[d][1]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if not visited[nx][ny]:
                visited[nx][ny] = room_num
                q.append((nx, ny))
    return room_size


def wall_remove():
    max_room = 0
    for i in range(m):
        for j in range(n):
            for d in range(4):
                ni = i + direction[d][0]
                nj = j + direction[d][1]

                if ni < 0 or ni >= m or nj < 0 or nj >= n:
                    continue
                if visited[i][j] != visited[ni][nj]:
                    a = room_sizes[visited[i][j]]
                    b = room_sizes[visited[ni][nj]]
                    max_room = max(max_room, a + b)
    return max_room


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
visited = [[0] * n for _ in range(m)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

room_sizes = [0]
room = 0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            room += 1
            room_size = bfs(i, j, room)
            room_sizes.append(room_size)
wall_remove_max_room = wall_remove()
print(room)
print(max(room_sizes))
print(wall_remove_max_room)

"""
"""
from sys import stdin
from collections import deque

input = stdin.readline


def bfs(i, j, room_num):
    q = deque()
    q.append((i, j))
    visited[i][j] = room_num
    room_size = 0
    while q:
        x, y = q.popleft()
        room_size += 1

        for d in range(4):
            nx = x + direction[d][0]
            ny = y + direction[d][1]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if not visited[nx][ny]:
                if (
                    # 북쪽방향 확인, 기존 칸에 북쪽 벽이 없는 경우
                    (d == 0 and board[x][y] & 2 == 0)
                    # 남쪽방향 확인, 기존 칸에 남쪽 벽이 없는 경우
                    or (d == 1 and board[x][y] & 8 == 0)
                    # 서쪽 방향 확인, 기존 칸에 서쪽 벽이 없는 경우
                    or (d == 2 and board[x][y] & 1 == 0)
                    # 동쪽 방향 확인, 기존 칸에 동쪽 벽이 없는 경우
                    or (d == 3 and board[x][y] & 4 == 0)
                ):
                    visited[nx][ny] = room_num
                    q.append((nx, ny))

    return room_size


def wall_remove():
    max_room = 0
    for i in range(m):
        for j in range(n):
            for d in range(4):
                ni = i + direction[d][0]
                nj = j + direction[d][1]

                if ni < 0 or ni >= m or nj < 0 or nj >= n:
                    continue
                if visited[i][j] != visited[ni][nj]:
                    a = room_sizes[visited[i][j]]
                    b = room_sizes[visited[ni][nj]]
                    max_room = max(max_room, a + b)
    return max_room


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
visited = [[0] * n for _ in range(m)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

room_sizes = [0]
room = 0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            room += 1
            room_size = bfs(i, j, room)
            room_sizes.append(room_size)
wall_remove_max_room = wall_remove()
print(room)
print(max(room_sizes))
print(wall_remove_max_room)
