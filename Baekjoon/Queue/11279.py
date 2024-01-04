"""
백준 - https://www.acmicpc.net/problem/11279

< 최대 힙 >
"""
import sys
import heapq

input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(q) != 0:
            _, num = heapq.heappop(q)
            print(num)
        else:
            print(0)
    else:
        heapq.heappush(q, (-x, x))
