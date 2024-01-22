"""
백준 - https://www.acmicpc.net/problem/1504

< 특정한 최단 경로 >
"""
import sys

input = sys.stdin.readline
import heapq

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

# 반드시 거쳐야 하는 정점 번호
v1, v2 = map(int, input().split())

distance = [int(1e9)] * (n + 1)
q = []
heapq.heappush(q, (v1, 0))
distance[v1] = 0

while q:
    node, d = heapq.heappop(q)

    if distance[node] < d:
        continue

    for next_node, dist in graph[node]:
        new_dist = distance[node] + dist
        if new_dist < distance[next_node]:
            distance[next_node] = new_dist
            heapq.heappush(q, (next_node, new_dist))

v1_1_dist = distance[1]
v1_v2_dist = distance[v2]
v1_n_dist = distance[n]


distance = [int(1e9)] * (n + 1)
q = []
heapq.heappush(q, (v2, 0))
distance[v2] = 0

while q:
    node, d = heapq.heappop(q)

    if distance[node] < d:
        continue

    for next_node, dist in graph[node]:
        new_dist = distance[node] + dist
        if new_dist < distance[next_node]:
            distance[next_node] = new_dist
            heapq.heappush(q, (next_node, new_dist))

v2_1_dist = distance[1]
v2_n_dist = distance[n]

a = v1_1_dist + v1_v2_dist + v2_n_dist
b = v2_1_dist + v1_v2_dist + v1_n_dist

if v1_v2_dist == int(1e9):
    a = b = -1

elif v1_1_dist == int(1e9) or v2_n_dist == int(1e9):
    a = -1

elif v2_1_dist == int(1e9) or v1_n_dist == int(1e9):
    b = -1


print(min(a, b))
