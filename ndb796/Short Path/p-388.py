'''
화성 탐사

1
3
5 5 4
3 9 1
3 2 7
'''
import sys
import heapq

input = sys.stdin.readline

t = int(input())
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
INF = int(1e9)

for _ in range(t):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    dp = [[INF] * n for _ in range(n)]
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    dp[0][0] = graph[0][0]

    while q:
        dist, x, y = heapq.heappop(q)

        if dp[x][y] < dist:
            continue

        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            cost = dist + graph[nx][ny]
            if cost < dp[nx][ny]:
                dp[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny)) 

    print(dp[-1][-1])
