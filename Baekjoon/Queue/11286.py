"""
백준 - https://www.acmicpc.net/problem/11286

< 절댓값 힙 >
"""
import sys
import heapq

input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if q:
            _, result = heapq.heappop(q)
            print(result)
        else:
            print(0)
    
    else:
        heapq.heappush(q, (abs(x), x))
