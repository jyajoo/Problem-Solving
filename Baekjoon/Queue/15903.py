"""
백준 - https://www.acmicpc.net/problem/15903

< 카드 합체 놀이 >
"""

import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
heapq.heapify(num)

for _ in range(m):
    x = heapq.heappop(num)
    y = heapq.heappop(num)
    heapq.heappush(num, x + y)
    heapq.heappush(num, x + y)

print(sum(num))
