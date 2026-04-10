"""
백준 - https://www.acmicpc.net/problem/11725

< 트리의 부모 찾기 >
"""

import sys
from collections import deque

input = sys.stdin.readline

def bfs(x):
    q = deque()
    q.append(x)
    visited = [False] * (n + 1)
    visited[x] = True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                parent[i] = now


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n + 1)
bfs(1)
print(*parent[2:], sep="\n")
