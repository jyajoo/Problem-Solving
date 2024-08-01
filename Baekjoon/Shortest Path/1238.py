"""
백준 - https://www.acmicpc.net/problem/1238

< 파티 >
"""

import sys
import heapq

input = sys.stdin.readline


def dijkstra(start, graph):
    distance = [int(1e9)] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for b, c in graph[now]:
            cost = dist + c
            if cost < distance[b]:
                distance[b] = cost
                heapq.heappush(q, (cost, b))
    return distance


n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
graph2 = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))
    graph2[e].append((s, t))

dist = dijkstra(x, graph)
dist2 = dijkstra(x, graph2)

result = -int(1e9)
for i in range(1, n + 1):
    result = max(result, dist[i] + dist2[i])
print(result)
