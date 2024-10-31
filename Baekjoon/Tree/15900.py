"""
백준 - https://www.acmicpc.net/problem/15900

< 나무 탈출 >
"""

import sys
from collections import deque

input = sys.stdin.readline


def bfs(current, dist):
    global distance
    q = deque()
    q.append((current, dist))
    visited = [False] * (n + 1)
    visited[1] = True
    while q:
        current, dist = q.popleft()
        if current != 1 and len(graph[current]) == 1:
            distance += dist
            continue

        for i in graph[current]:
            if not visited[i]:
                visited[i] = True
                q.append((i, dist + 1))


n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트노드에서 각 리프 노드까지의 총 거리의 수가 홀수여야 한다.
# 그래야 마지막 움직임을 성원이가 하게 되고, 형석이를 이길 수 있다.

distance = 0
bfs(1, 0)

if distance % 2 != 0:
    print("Yes")
else:
    print("No")
