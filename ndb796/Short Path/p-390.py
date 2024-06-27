'''
< 숨바꼭질 >
6 7 
3 6
4 3
3 2
1 3
1 2
2 4
5 2
'''
import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = []
start = 1 
heapq.heappush(q, (0, start))
distance = [INF] * (n + 1)
distance[start] = 0
while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue

    for i in graph[now]:
        cost = dist + 1
        if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(q, (cost, i))

a = distance.index(max(distance[1:]))
b = distance[a]
c = distance.count(b)
print(a, b, c)