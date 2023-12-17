"""
백준 - https://www.acmicpc.net/problem/15650

< N과 M (2) >
"""
import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = [i for i in range(1, n + 1)]
lst = list(combinations(numbers, m))

for i in lst:
    print(*i)

"""
"""
import sys

def dfs(arr, x):
    if len(arr) == m:
        print(*arr)
    
    for i in range(x, n + 1):
        if i not in arr:
            dfs(arr + [i], i)

input = sys.stdin.readline

n, m = map(int, input().split())
dfs([], 1)