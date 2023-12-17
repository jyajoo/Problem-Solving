"""
백준 - https://www.acmicpc.net/problem/15652

< N과 M (4) >
"""
import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = [i for i in range(1, n + 1)]
lst = list(combinations_with_replacement(numbers, m))

for i in lst:
    print(*i)

"""
"""
import sys

def dfs(arr, x):
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(x, n + 1):
        dfs(arr + [i], i)


input = sys.stdin.readline

n, m = map(int, input().split())
dfs([], 1)