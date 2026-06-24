'''
백준 - https://www.acmicpc.net/problem/18352

< 특정 거리의 도시 찾기 >
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    global visited, answer
    q = deque()
    q.append((start, 0))
    visited[start] = True

    while q:
        x, dist = q.popleft()
        if dist == k:
            answer.append(x)
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                q.append((i, dist + 1))

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

answer = []
visited = [False] * (n + 1)
bfs(x)
answer.sort()
if len(answer) == 0:
    print(-1)
else:
    for i in answer:
        print(i)