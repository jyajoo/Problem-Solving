'''
백준 - https://www.acmicpc.net/problem/1260

< DFS와 BFS >

'''
from collections import deque


def dfs(v):
    visited[v] = True
    print(v + 1, end=" ")
    for i in arr[v]:
        if not visited[i]:
            dfs(i)


def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v + 1, end=" ")
        for i in arr[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split())
arr = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    x, y = map(int, input().split())
    arr[x-1].append(y-1)
    arr[y-1].append(x-1)

for i in range(n):
    arr[i].sort()

dfs(v - 1)
print()

visited = [False] * n
bfs(v - 1)
