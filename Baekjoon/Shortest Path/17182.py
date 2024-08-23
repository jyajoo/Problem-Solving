"""
백준 - https://www.acmicpc.net/problem/17182

< 우주 탐사선 >
"""

from sys import stdin

input = stdin.readline


def find_route(k, result, cnt):
    global answer
    if cnt == n:
        answer = min(answer, result)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            find_route(i, result + graph[k][i], cnt + 1)
            visited[i] = False


n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        for x in range(n):
            graph[i][j] = min(graph[i][j], graph[i][x] + graph[x][j])


answer = int(1e9)
visited = [False] * n
visited[k] = True
find_route(k, 0, 1)
print(answer)
