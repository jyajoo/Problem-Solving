"""
백준 - https://www.acmicpc.net/problem/15649

< N과 M (1) >
"""
import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = [i for i in range(1, n + 1)]
lst = list(permutations(numbers, m))

for i in lst:
    print(*i)


"""
"""
import sys


def dfs(x, arr):
    if x == m:
        result.append(arr)
        return

    for i in numbers:
        if i not in arr:
            dfs(x + 1, arr + [i])


input = sys.stdin.readline
n, m = map(int, input().split())
numbers = [i for i in range(1, n + 1)]
result = []
dfs(0, [])

for i in result:
    print(*i)

"""
"""
import sys


def dfs():
    if len(s) == m:
        print(*s)
        return

    for i in range(1, n + 1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()


input = sys.stdin.readline
n, m = list(map(int, input().split()))
s = []
dfs()
