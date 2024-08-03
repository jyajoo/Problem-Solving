"""
백준 - https://www.acmicpc.net/problem/1941

< 소문난 칠공주 >
"""
import sys
from collections import deque

input = sys.stdin.readline

board = [list(input().strip()) for _ in range(5)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

s_list = []
y_list = []
for i in range(5):
    for j in range(5):
        if board[i][j] == "S":
            s_list.append((i, j))
        if board[i][j] == "Y":
            y_list.append((i, j))


def combi(arr, data, r, result):
    if len(data) == r:
        result.append(data)
        return

    for i in range(len(arr)):
        new_data = data + [arr[i]]
        new_arr = arr[i + 1 :]
        combi(new_arr, new_data, r, result)


answer = 0
for i in range(4, 8):
    s_result = []
    combi(s_list, [], i, s_result)

    if len(s_result) == 0:
        break

    y_result = []
    combi(y_list, [], 7 - i, y_result)

    for s_points in s_result:
        for y_points in y_result:
            points = s_points + y_points
            visited = [[False] * 5 for _ in range(5)]
            q = deque()
            x, y = points[0]
            q.append((x, y))
            visited[x][y] = True
            count = 1
            while q:
                x, y = q.popleft()
                for dx, dy in direction:
                    nx = x + dx
                    ny = y + dy
                    if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                        continue
                    if (nx, ny) in points and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        count += 1

            if count == 7:
                answer += 1

print(answer)
