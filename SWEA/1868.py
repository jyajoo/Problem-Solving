'''
SWEA - https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AV5LwsHaD1MDFAXc&categoryId=AV5LwsHaD1MDFAXc&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=1

< 파핑파핑 지뢰찾기 >
'''
from collections import deque
import sys

sys.stdin = open("C:\Coding\GitHub\Algorithm\SWEA\input (2).txt", "r")

def check_land_mine(i, j):
    land_mine = 0
    for dx, dy in direction:
        nx, ny = i + dx, j + dy
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == '*':
                land_mine += 1
    board[i][j] = land_mine

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    board[i][j] = '*'
    while queue:
        i, j = queue.popleft()
        for dx, dy in direction:
            nx, ny = i + dx, j + dy
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0:
                    board[nx][ny] = '*'
                    queue.append((nx, ny))
                elif board[nx][ny] != '*':
                    board[nx][ny] = '*'



T = int(input())
direction = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
for t in range(T):
    n = int(input())
    board= [list(input()) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                check_land_mine(i, j)
    
    answer = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                answer += 1
                bfs(i, j)

    for i in range(n):
        for j in range(n):
            if board[i][j] != '*':
                answer += 1
    print("#{} {}".format(t + 1, answer))

'''
2
3
..*
..*
**.
5
..*..
..*..
.*..*
.*...
.*...

02*20
13*31
2*32*
3*311
2*200

'''