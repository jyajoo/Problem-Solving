"""
백준 - https://www.acmicpc.net/problem/22233

< 가희와 키워드 >
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
memo_keywords = dict()
for _ in range(n):
    keyword = input().strip()
    if keyword not in memo_keywords:
        memo_keywords[keyword] = 1

for _ in range(m):
    arr = input().strip().split(",")
    for keyword in arr:
        if keyword in memo_keywords:
            del memo_keywords[keyword]
    print(len(memo_keywords))
