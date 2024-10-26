"""
백준 - https://www.acmicpc.net/problem/3584

< 가장 가까운 공통 조상 >
"""

import sys
from collections import deque

input = sys.stdin.readline

t = int(input())


def find_parent(x):
    if union[x] < 0:
        return x
    else:
        union[x] = find_parent(union[x])
        return union[x]


def find_union(a, b):
    x = find_parent(a)
    y = find_parent(b)
    if x == y:
        return False
    else:
        union[x] += union[y]
        union[y] = x
        return True


for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    graph2 = [[] for _ in range(n + 1)]
    union = [-1] * (n + 1)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph2[b].append(a)
        find_union(a, b)

    a, b = map(int, input().split())

    total_parent = find_parent(1)

    depth = 1
    q = deque()
    q.append((depth, total_parent))
    depths = [0] * (n + 1)

    while q:
        depth, now = q.popleft()
        depths[now] = depth
        for i in graph[now]:
            q.append((depth + 1, i))

    while True:
        if depths[a] != depths[b]:
            if depths[a] < depths[b]:
                b = graph2[b][0]
            else:
                a = graph2[a][0]
        else:
            break

    q = deque()
    q.append(a)
    q2 = deque()
    q2.append(b)
    while q or q2:
        if len(q) == 0 or len(q2) == 0:
            if len(q) != 0:
                print(q.pop())
                break
            else:
                print(q2.pop())
                break

        a = q.popleft()
        b = q2.popleft()
        if a == b:
            print(a)
            break

        for i in graph2[a]:
            q.append(i)

        for i in graph2[b]:
            q2.append(i)
"""
"""
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    parent = [0] * (n + 1)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        parent[b] = a  # b의 부모를 a로 설정

    a, b = map(int, input().split())

    arr = []  # a가 제일 공통 부모까지 도달하는 루트
    temp = a
    while True:
        arr.append(temp)
        if parent[temp] == 0:
            break
        temp = parent[temp]

    # b도 공통 부모까지 올라가면서, a의 루트에 포함되어있는지 확인
    temp = b
    while True:
        if temp in arr:
            print(temp)
            break
        temp = parent[temp]
