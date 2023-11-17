"""
SWEA - https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AV14vXUqAGMCFAYD&categoryId=AV14vXUqAGMCFAYD&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=1&&&&&&&&&&

< [S/W 문제해결 기본] 7일차 - 미로1 > 
"""
import sys

sys.stdin = open("C:\Coding\GitHub\Algorithm\SWEA\input (2).txt", "r")

from collections import deque

def bfs(x, y):
    global answer
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 16 and 0 <= ny < 16:
                if miro[nx][ny] == 3:
                    answer = 1
                    return
                if miro[nx][ny] == 0 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(10):
    T = int(input())
    miro = [list(map(int, input())) for _ in range(16)]
    visited = [[False for _ in range(16)] for _ in range(16)]
    answer = 0
    bfs(1, 1)
    print("#{} {}".format(T, answer))