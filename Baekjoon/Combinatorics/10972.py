"""
백준 - https://www.acmicpc.net/problem/10972

< 다음 순열 >
"""

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

idx = -1
for i in range(n - 1, 0, -1):
    if arr[i] > arr[i - 1]:  # 오름차순
        idx = i
        break

if idx == -1:
    print(-1)

else:
    for j in range(n - 1, idx - 1, -1):
        if arr[j] > arr[idx - 1]:
            arr[idx - 1], arr[j] = arr[j], arr[idx - 1]
            break

    arr[idx:] = arr[idx:][::-1]
    print(*arr)
