"""
구름톤 챌린지 - https://level.goorm.io/exam/195696/%EC%9E%91%EC%9D%80-%EB%85%B8%EB%93%9C/quiz/1

< 작은 노드 >
- 비재귀 dfs
"""
import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    s, e = map(int, input().split())
    if e not in graph[s]:
        graph[s].append(e)
    if s not in graph[e]:
        graph[e].append(s)

for i in range(n + 1):
    graph[i].sort()
result = []


# 비재귀 dfs
def dfs(k):
    stack = [k]
    visited[k] = True
    result.append(k)
    while stack:
        k = stack.pop()
        for i in graph[k]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True
                result.append(i)
                break


dfs(k)
# print(result)
print(visited.count(True), result[-1])
"""
- 재귀 dfs
"""
import sys

sys.setrecursionlimit(10**4)
input = sys.stdin.readline


def dfs(k):
    for i in sorted(graph[k]):
        if not visited[i]:
            visited[i] = True
            return dfs(i)
    else:
        return k


n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
visited[k] = True
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited[k] = True
result = dfs(k)
print(visited.count(True), result)
