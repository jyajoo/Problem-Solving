"""
백준 - https://www.acmicpc.net/problem/20366

< 같이 눈사람 만들래? >
"""

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = sys.maxsize

for start in range(n - 3):
    for end in range(start + 3, n):
        height = arr[start] + arr[end]

        s, e = start + 1, end - 1
        while s < e:
            height2 = arr[s] + arr[e]
            result = min(result, abs(height - height2))
            if height2 < height:
                s += 1
            elif height2 > height:
                e -= 1
            else:
                print(0)
                exit()
print(result)
