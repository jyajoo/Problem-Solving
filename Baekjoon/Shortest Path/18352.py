'''
백준 - https://www.acmicpc.net/problem/18352

< 특정 거리의 도시 찾기 >
- 1부터 n까지의 m개의 단방향 도로가 존재
- 모든 도로의 거리는 1
- x에서 출발하여 도달할 수 있는 모든 도시 중 최단 거리가 k인 번호 출력
- x에서 x로 가는 최단 거리는 항상 0

2 <= n <= 300000
1 <= m <= 1000000
1 <= k <= 300000
1 <= x <= n
시간복잡도 <= O(N)
'''
'''
다익스트라 최단 경로 알고리즘
시간 복잡도는 O(MlogN)
'''
import sys, heapq
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

distance = [int(1e9)] * (n + 1)

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

dijkstra(x)
result = []
for i in range(1, n + 1):
    if distance[i] == k:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    for i in result:
        print(i)
