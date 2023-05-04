"""
< 전보 >
"""
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(c):
    distance[c] = 0
    q = []
    heapq.heappush(q, (0, c))
    while q:
        now_dist, now_node = heapq.heappop(q)
        if now_dist > distance[now_node]:
            continue

        for y, z in graph[now_node]:
            cost = distance[now_node] + z
            if cost < distance[y]:
                distance[y] = cost
                heapq.heappush(q, (cost, y))


dijkstra(c)
count = 0
time = 0
for i in distance:
    if i != INF and i != 0:
        count += 1
        time = max(time, i)

print(count, time)
