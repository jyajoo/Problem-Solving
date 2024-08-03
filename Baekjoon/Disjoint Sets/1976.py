"""
백준 - https://www.acmicpc.net/problem/1976

< 여행 가자 >
"""

import sys
from collections import deque

input = sys.stdin.readline


def dfs(start, end):
    q = deque()
    q.append((start, start))
    visited = [[False] * n for _ in range(n)]
    visited[start][start] = True

    while q:
        s, e = q.popleft()
        if e == end:
            return True

        for idx, x in enumerate(graph[e]):
            if x == 1 and not visited[e][idx]:
                visited[e][idx] = True
                q.append((e, idx))

    return False


n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

plan = list(map(int, input().split()))

result = "YES"
for i in range(1, m):
    start = plan[i - 1] - 1
    end = plan[i] - 1
    if not dfs(start, end):
        result = "NO"
        break
print(result)
"""
"""
import sys

input = sys.stdin.readline


def find_parent(x):
    if union[x] < 0:
        return x
    else:
        union[x] = find_parent(union[x])
        return union[x]


def find_union(x, y):
    a = find_parent(x)
    b = find_parent(y)

    if a == b:
        return False
    else:
        union[a] += union[b]
        union[b] = a
        return True


n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

plan = list(map(int, input().split()))

union = [-1] * n
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            find_union(i, j)

start = find_parent(plan[0] - 1)
result = "YES"
for i in range(1, m):
    if find_parent(plan[i] - 1) != start:
        result = "NO"
        break
print(result)
