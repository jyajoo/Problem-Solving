"""
백준 - https://www.acmicpc.net/problem/1446

< 지름길 >
"""
from sys import stdin
import heapq

def dijkstra(start):
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

input = stdin.readline

n, d = map(int, input().split())

graph = [[] for _ in range(d + 1)]
distance = [int(1e9)] * (d + 1)

for _ in range(n):
    s, e, l = map(int, input().split())
    if e <= d:
        graph[s].append((e, l))

for i in range(d):
    graph[i].append((i + 1, 1))

dijkstra(0)
print(distance[d])
'''
'''
from sys import stdin

input = stdin.readline

n, d = map(int, input().split())

distance = [i for i in range(d + 1)]

shortcuts = [list(map(int, input().split())) for _ in range(n)]

for i in range(d + 1):
    distance[i] = min(distance[i], distance[i - 1] + 1)

    for s, e, l in shortcuts:
        if e == i:
            distance[e] = min(distance[e], distance[s] + l)

print(distance[d])
