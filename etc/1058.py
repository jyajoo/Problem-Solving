'''
백준 - https://www.acmicpc.net/problem/1058

< 친구 >
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    global answer
    q = deque()
    visited = [False] * n
    visited[start] = True
    q.append((start, 0))
    count = 0
    while q:
        x, depth = q.popleft()
        if depth == 2:
            continue
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                q.append((i, depth + 1))
                count += 1
    answer = max(answer, count)

n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    for idx, j in enumerate(input().strip()):
        if j == 'Y':
            graph[i].append(idx)

answer = 0
for i in range(n):
    bfs(i)

print(answer)