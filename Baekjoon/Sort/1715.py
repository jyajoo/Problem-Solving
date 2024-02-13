"""
백준 - https://www.acmicpc.net/problem/1715

< 카드 정렬하기 >
"""

import sys
import heapq

input = sys.stdin.readline
n = int(input())
cards = []

for _ in range(n):
    heapq.heappush(cards, int(input()))

answer = 0

while len(cards) != 1:
    num1 = heapq.heappop(cards)
    num2 = heapq.heappop(cards)
    answer += num1 + num2
    heapq.heappush(cards, num1 + num2)

print(answer)