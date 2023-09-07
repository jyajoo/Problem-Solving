'''
구름톤 챌린지 - https://level.goorm.io/exam/195701/%EB%8C%80%EC%B2%B4-%EA%B2%BD%EB%A1%9C/quiz/1

< 대체 경로 >
'''
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra():
    q = []
    heapq.heappush(q, (1, s))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for n in graph[now]:
            if n != i:
                cost = dist + 1
                if cost < distance[n] :
                    distance[n] = cost
                    heapq.heappush(q,(cost, n))


n, m, s, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, U = map(int, input().split())
    graph[u].append(U)
    graph[U].append(u)

for i in range(1, n + 1):
    if s == i or e == i:
        print(-1)
        continue
    distance = [INF] * (n + 1)
    distance[s] = 1
    dijkstra()

    if distance[e] == INF:
        print(-1)
    else:
        print(distance[e])