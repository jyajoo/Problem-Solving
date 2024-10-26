"""
백준 - https://www.acmicpc.net/problem/19637

< IF문 좀 대신 써줘 >
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
names = []
for _ in range(n):
    name, skill = input().split()
    names.append((name, int(skill)))

# 스킬 값을 기준으로 정렬
names.sort(key=lambda x: x[1])

for _ in range(m):
    current_skill = int(input())
    start, end = 0, n - 1
    while start <= end:
        middle = (start + end) // 2
        name, skill = names[middle]
        if current_skill <= skill:
            end = middle - 1
        elif current_skill > skill:
            start = middle + 1
    print(names[start][0])
"""
"""
from bisect import bisect_left
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
names = []
skills = []
for _ in range(n):
    name, skill = input().split()
    names.append(name)
    skills.append(int(skill))

for _ in range(m):
    current_skill = int(input())
    print(names[bisect_left(skills, current_skill)])
