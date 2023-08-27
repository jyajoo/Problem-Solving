"""
백준 - https://www.acmicpc.net/problem/18352

< 특정 거리의 도시 찾기 >
"""
import sys
from collections import deque

input = sys.stdin.readline
# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호
n, m, k, x = map(int, input().split())

# 도로
road = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
visited[x] = True
for _ in range(m):
    a, b = map(int, input().split())
    road[a].append(b)

# bfs로 최단 거리 찾기
result = [-1] * (n + 1)
result[x] = 0
# result = [0] * (n + 1)


def bfs(x, road):
    queue = deque([x])
    while queue:
        v = queue.popleft()
        for i in road[v]:
            if not visited[i]:
                visited[i] = True
                result[i] = result[v] + 1
                queue.append(i)


bfs(x, road)
exist = False
for i in range(1, n + 1):
    if result[i] == k:
        exist = True
        print(i)
if not exist:
    print(-1)
