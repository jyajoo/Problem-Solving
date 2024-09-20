"""
백준 - https://www.acmicpc.net/problem/20920

< 영단어 암기는 괴로워 >
"""

import sys
from collections import Counter

input = sys.stdin.readline

# 단어의 개수, 외울 단어의 길이 기준
n, m = map(int, input().split())

words = [input().rstrip() for _ in range(n)]
filter_words = [w for w in words if len(w) >= m]
count = dict(Counter(filter_words))

result = list(count.items())
result.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))
for x, _ in result:
    print(x)
