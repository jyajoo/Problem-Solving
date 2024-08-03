"""
백준 - https://www.acmicpc.net/problem/1700

< 멀티탭 스케줄링 >
"""

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
current = []
for i in range(k):
    if arr[i] not in current:
        if len(current) < n:
            current.append(arr[i])
        else:
            new_arr = arr[i + 1 :]
            max_idx = -1
            val_idx = -1
            for idx, x in enumerate(current):
                if x in new_arr:
                    x_idx = new_arr.index(x)
                    if x_idx > max_idx:
                        max_idx = x_idx
                        val_idx = idx
                else:
                    val_idx = idx
                    break

            current[val_idx] = arr[i]
            result += 1
print(result)
