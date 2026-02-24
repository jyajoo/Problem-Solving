'''
백준 - https://www.acmicpc.net/problem/10655

< 마라톤 1 >
'''
import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

total = 0
for i in range(n - 1):
    x1, y1 = arr[i]
    x2, y2 = arr[i + 1]
    total += abs(x1 - x2) + abs(y1 - y2)

answer = int(1e9)
for i in range(1, n - 1):
    x0, y0 = arr[i - 1]
    x1, y1 = arr[i]
    x2, y2 = arr[i + 1]

    dist1 = abs(x0 - x1) + abs(y0 - y1)
    dist2 = abs(x1 - x2) + abs(y1 - y2)
    dist3 = abs(x0 - x2) + abs(y0 - y2)

    answer = min(answer, total - dist1 - dist2 + dist3)

print(answer)
