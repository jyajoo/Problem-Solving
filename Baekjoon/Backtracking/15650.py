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