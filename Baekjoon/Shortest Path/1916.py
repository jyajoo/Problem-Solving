'''
백준 - https://www.acmicpc.net/problem/1916

< 최소비용 구하기 >

n개의 도시, m개의 버스
a에서 b로 가는 최소 비용
'''
'''
다익스트라 최단 경로 알고리즘
시간 복잡도 O(MlogN)
'''
import sys, heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())
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

dijkstra(start)
print(distance[end])