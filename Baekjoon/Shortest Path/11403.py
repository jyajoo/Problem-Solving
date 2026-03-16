'''
백준 - https://www.acmicpc.net/problem/11403

< 경로 찾기 >
'''
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result[i][j] = 1
            q = deque()
            q.append(j)
            visited = [False] * n
            visited[j] = True
            while q:
                now = q.popleft()
                for idx, k in enumerate(graph[now]):
                    if k and not visited[idx]:
                        visited[idx] = True
                        result[i][idx] = 1
                        q.append(idx)

for i in result:
    print(*i)
'''
'''
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = [[0] * n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1
            
for i in graph:
    print(*i)
