"""
백준 - https://www.acmicpc.net/problem/20922

< 겹치는 건 싫어 >
"""

import sys
from collections import defaultdict

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
cnt = defaultdict(int)

end = 0
result = 0

for start in range(n):
    while end < n:
        if cnt[arr[end]] < k:
            cnt[arr[end]] += 1
            end += 1
            result = max(result, end - start)
        else:

            break
    cnt[arr[start]] -= 1

print(result)
