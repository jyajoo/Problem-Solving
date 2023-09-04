"""
구름톤 챌린지 - https://level.goorm.io/exam/195698/%EC%97%B0%ED%95%A9/quiz/1

< 연합 > 
"""
import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(1000)


def find_parent(x):
    if parent[x] != x:
        return find_parent(parent[x])
    else:
        return x


def union_parent(s, e):
    s = find_parent(s)
    e = find_parent(e)
    if s < e:
        parent[e] = s
    else:
        parent[s] = e


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
parent = [i for i in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    if s in graph[e]:
        union_parent(s, e)

result = []
for i in range(1, n + 1):
    if find_parent(i) not in result:
        result.append(find_parent(i))

print(len(result))
