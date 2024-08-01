"""
백준 - https://www.acmicpc.net/problem/15651

< N과 M (3) >
"""
import sys
from itertools import product
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = [i for i in range(1, n + 1)]
lst = list(product(numbers, repeat = m))
for i in lst:
    print(*i)
# print("\n".join(list(map(" ".join, product(num, repeat=m)))))

"""
"""
import sys

def dfs(arr):
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(1, n + 1):
        dfs(arr + [i])

input = sys.stdin.readline

n, m = map(int, input().split())
dfs([])
