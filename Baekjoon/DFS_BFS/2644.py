'''
백준 - https://www.acmicpc.net/problem/2644

< 촌수계산 >
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    global answer
    q = deque()
    q.append((x, 0))
    visited[x] = True
    while q:
        now, count = q.popleft()
        print(now, count)
        if now == b:
            answer = count
            break
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append((i, count + 1))


n = int(input())
a, b = map(int, input().split())

graph = [[] for _ in range(n + 1)]
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

answer = -1
visited = [False] * (n + 1)
bfs(a)
print(answer)