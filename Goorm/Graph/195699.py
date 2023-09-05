"""
구름톤 챌린지 - https://level.goorm.io/exam/195699/%EA%B7%B8%EB%9E%98%ED%94%84%EC%9D%98-%EB%B0%80%EC%A7%91%EB%8F%84/quiz/1

< 그래프의 밀집도 >
"""
import sys
from collections import defaultdict

input = sys.stdin.readline


def find_parent(a):
    if parent[a] != a:
        return find_parent(parent[a])
    else:
        return a


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
parent = [i for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    union(a, b)

union = defaultdict(list)
for i in range(1, n + 1):
    p = find_parent(i)
    union[p] += [i]

result = []
for values in union.values():
    count = 0
    for j in values:
        count += len(graph[j])
    result.append((count / len(values), len(values), min(values), values))

result.sort(key=lambda x: (-x[0], x[1], x[2]))

for i in result[0][3]:
    print(i, end=" ")
