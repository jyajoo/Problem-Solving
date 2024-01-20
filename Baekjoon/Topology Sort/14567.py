"""
백준 - https://www.acmicpc.net/problem/14567

< 선수과목 (Prerequisite) >
"""
import sys

input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
result = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)
        result[i] += 1

while q:
    node = q.popleft()
    step = result[node]
    for next_node in graph[node]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            q.append(next_node)
            result[next_node] = step + 1

print(*result[1:])
