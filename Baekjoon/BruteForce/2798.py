"""
백준 - https://www.acmicpc.net/problem/2798

< 블랙잭 >
"""
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

answer = 0
for i in combinations(cards, 3):
    if sum(i) <= m:
        answer = max(answer, sum(i))

print(answer)