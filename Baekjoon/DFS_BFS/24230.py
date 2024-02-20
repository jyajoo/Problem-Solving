'''
백준 - https://www.acmicpc.net/problem/24230

< 트리 색칠하기 >
'''
import sys

input = sys.stdin.readline

def dfs(x):
    for i in graph[x]:
        if info[i] == info[x] and not visited[i]:
            visited[i] = True
            dfs(i)
            info[i] = 0
    info[x] = 0

n = int(input())
info = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
answer = 0
for i in range(n, 0, -1):
    if info[i] != 0 and not visited[i]:
        visited[i] = True
        dfs(i)
        answer += 1
print(answer)
'''
'''
import sys

input = sys.stdin.readline
n = int(input())
info = [0] + list(map(int, input().split()))
count = 0
if info[1] != 0:
    count += 1
for _ in range(n - 1):
    a, b = map(int, input().split())
    if info[a] != info[b]:
        count += 1
print(count)