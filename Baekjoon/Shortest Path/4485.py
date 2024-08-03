"""
백준 - https://www.acmicpc.net/problem/4485

< 녹색 옷 입은 애가 젤다지? >
"""

import sys
import heapq

input = sys.stdin.readline
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
i = 1
while True:
    n = int(input())
    if n == 0:
        break
    board = [list(map(int, input().split())) for _ in range(n)]
    coins = [[int(1e9)] * n for _ in range(n)]
    q = []
    heapq.heappush(q, (board[0][0], 0, 0))
    coins[0][0] = board[0][0]
    while q:
        coin, x, y = heapq.heappop(q)
        if coins[x][y] < coin:
            continue

        for dx, dy in direction:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            new_coin = coin + board[nx][ny]
            if new_coin < coins[nx][ny]:
                coins[nx][ny] = new_coin
                heapq.heappush(q, (new_coin, nx, ny))

    print("Problem {}: {}".format(i, coins[-1][-1]))
    i += 1
