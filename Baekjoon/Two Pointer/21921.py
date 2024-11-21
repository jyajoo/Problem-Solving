"""
백준 - https://www.acmicpc.net/problem/21921

< 블로그 >
"""

import sys

input = sys.stdin.readline
n, x = map(int, input().split())
arr = list(map(int, input().split()))

count = 1
max_val = sum(arr[:x])
answer = max_val
for start in range(n - x):
    max_val -= arr[start]
    max_val += arr[start + x]
    if answer < max_val:
        answer = max_val
        count = 1
    elif answer == max_val:
        count += 1

if answer != 0:
    print(answer)
    print(count)
else:
    print("SAD")
