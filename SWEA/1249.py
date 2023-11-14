"""
SWEA - https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AV15QRX6APsCFAYD&categoryId=AV15QRX6APsCFAYD&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=1

< [S/W 문제해결 응용] 4일차 - 보급로 >
"""

import sys
import heapq

sys.stdin = open("C:\coding\github\Algorithm\SWEA\input (1).txt", "r")


def dijkstra(x, y):
    q = []
    heapq.heappush(q, (x, y, 0))
    distance[x][y] = 0

    while q:
        x, y, dist = heapq.heappop(q)

        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if dist + numbers[nx][ny] < distance[nx][ny]:
                    distance[nx][ny] = dist + numbers[nx][ny]
                    heapq.heappush(q, (nx, ny, dist + numbers[nx][ny]))

T = int(input())
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for t in range(T):
    N = int(input())
    numbers = []
    for _ in range(N):
        numbers.append(list(map(int, input())))

    distance = [[int(1e9) for _ in range(N)] for _ in range(N)]

    dijkstra(0, 0)

    print("#{} {}".format(t + 1, distance[-1][-1]))