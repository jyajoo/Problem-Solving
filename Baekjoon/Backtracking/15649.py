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
