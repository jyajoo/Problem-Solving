"""
SWEA - https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AV7I5fgqEogDFAXB&categoryId=AV7I5fgqEogDFAXB&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=1

< 격자판의 숫자 이어 붙이기 >
"""
from collections import deque

T = int(input())
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(i, j):
    global result
    queue = deque()
    queue.append((i, j, str(board[i][j])))
    while queue:
        i, j, number = queue.popleft()
        if len(number) == 7:
            result.append(number)
            continue

        for dx, dy in direction:
            nx = i + dx
            ny = j + dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                queue.append((nx, ny, number + str(board[nx][ny])))
            



for t in range(T):
    board = [list(map(int, input().split())) for _ in range(4)]

    result = []
    for i in range(4):
        for j in range(4):
            bfs(i, j)
    print("#{} {}".format(t + 1, len(set(result))))
"""
1
1 1 1 1
1 1 1 2
1 1 2 1
1 1 1 1
"""
