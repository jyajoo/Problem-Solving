"""
백준 - https://www.acmicpc.net/problem/20040

< 사이클 게임 >
"""
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

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


n, m = map(int, input().split())
union = [-1] * n

lines = []
for i in range(m):
    a, b = map(int, input().split())
    lines.append((a, b))

result = 0
for i in range(m):
    a, b = lines[i]
    if not find_union(a, b):
        result = i + 1
        break

print(result)
