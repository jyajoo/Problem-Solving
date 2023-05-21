"""
백준 - https://www.acmicpc.net/problem/1647

< 도시 분할 계획 >
"""


def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])
last = 0

for a, b, c in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += c
        last = c

print(result - last)
