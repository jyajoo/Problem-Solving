"""
백준 - https://www.acmicpc.net/problem/22233

< 가희와 키워드 >
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
memo_keywords = set(input().strip() for _ in range(n))
for _ in range(m):
    arr = set(input().strip().split(","))
    memo_keywords -= arr
    print(len(memo_keywords))
