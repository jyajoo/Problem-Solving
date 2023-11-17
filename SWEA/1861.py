"""
SWEA - https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AV5LtJYKDzsDFAXc&categoryId=AV5LtJYKDzsDFAXc&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=1

< 정사각형 방 >
"""
import sys

sys.stdin = open("C:\coding\github\Algorithm\SWEA\input.txt", "r")

def dfs(i, j):
    stack = []
    stack.append((i, j))
    count = 0
    while stack:
        i, j = stack.pop()
        count += 1
        for dx, dy in direction:
            nx, ny = i + dx, j + dy
            if 0 <= nx < n and 0 <= ny < n:
                if rooms[i][j] + 1 == rooms[nx][ny]:
                    stack.append((nx, ny))
    return count

T = int(input())
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for t in range(T):
    n = int(input())
    rooms = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    start_room = int(1e9)
    for i in range(n):
        for j in range(n):
            count = dfs(i, j)
            if answer < count:
                answer = count
                start_room = rooms[i][j]
            elif answer == count:
                start_room = min(start_room, rooms[i][j])


    print("#{} {} {}".format(t + 1, start_room, answer))
