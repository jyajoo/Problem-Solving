"""
백준 - https://school.programmers.co.kr/learn/courses/30/lessons/60063

< 블록 이동하기 >
"""
import sys
from collections import deque

input = sys.stdin.readline


def find_next_robots(robot, board):
    n = len(board)
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    next_robots = []
    x1, y1 = robot[0][0], robot[0][1]
    x2, y2 = robot[1][0], robot[1][1]

    # 상하좌우 확인하기
    for dx, dy in direction:
        nx1, ny1 = x1 + dx, y1 + dy
        nx2, ny2 = x2 + dx, y2 + dy
        if (
            0 <= nx1 < n
            and 0 <= ny1 < n
            and 0 <= nx2 < n
            and 0 <= ny2 < n
            and board[nx1][ny1] == board[nx2][ny2] == 0
        ):
            next_robots.append({(nx1, ny1), (nx2, ny2)})

    if x1 == x2:
        for i in [-1, 1]:
            if (
                0 <= x1 + i < n
                and 0 <= x2 + i < n
                and board[x1 + i][y1] == board[x2 + i][y2] == 0
            ):
                next_robots.append({(x1, y1), (x1 + i, y1)})
                next_robots.append({(x2, y2), (x2 + i, y2)})

    elif y1 == y2:
        for i in [-1, 1]:
            if (
                0 <= y1 + i < n
                and 0 <= y2 + i < n
                and board[x1][y1 + i] == board[x2][y2 + i] == 0
            ):
                next_robots.append({(x1, y1), (x1, y1 + i)})
                next_robots.append({(x2, y2), (x2, y2 + i)})
    return next_robots


def solution(board):
    robot = {(0, 0), (0, 1)}
    q = deque()
    q.append((robot, 0))
    visited = [robot]
    n = len(board)
    while q:
        robot, count = q.popleft()
        if (n - 1, n - 1) in robot:
            return count

        next_robots = find_next_robots(list(robot), board)
        for next_robot in next_robots:
            if next_robot not in visited:
                visited.append(next_robot)
                q.append((next_robot, count + 1))


board = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0],
]

print(solution(board))

"""
외곽벽을 추가하기
"""
import sys
from collections import deque

input = sys.stdin.readline


def find_next_robots(robot, board):
    n = len(board)
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    next_robots = []
    x1, y1 = robot[0][0], robot[0][1]
    x2, y2 = robot[1][0], robot[1][1]

    # 상하좌우 확인하기
    for dx, dy in direction:
        nx1, ny1 = x1 + dx, y1 + dy
        nx2, ny2 = x2 + dx, y2 + dy
        if board[nx1][ny1] == board[nx2][ny2] == 0:
            next_robots.append({(nx1, ny1), (nx2, ny2)})

    if x1 == x2:
        for i in [-1, 1]:
            if board[x1 + i][y1] == board[x2 + i][y2] == 0:
                next_robots.append({(x1, y1), (x1 + i, y1)})
                next_robots.append({(x2, y2), (x2 + i, y2)})

    elif y1 == y2:
        for i in [-1, 1]:
            if board[x1][y1 + i] == board[x2][y2 + i] == 0:
                next_robots.append({(x1, y1), (x1, y1 + i)})
                next_robots.append({(x2, y2), (x2, y2 + i)})
    return next_robots


def solution(board):
    robot = {(1, 1), (1, 2)}
    q = deque()
    q.append((robot, 0))
    visited = [robot]
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    print(new_board)
    while q:
        robot, count = q.popleft()
        if (n, n) in robot:
            return count

        next_robots = find_next_robots(list(robot), new_board)
        for next_robot in next_robots:
            if next_robot not in visited:
                visited.append(next_robot)
                q.append((next_robot, count + 1))


board = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0],
]

print(solution(board))
