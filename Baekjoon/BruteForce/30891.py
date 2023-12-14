"""
백준 - https://www.acmicpc.net/problem/30891

< 볶음밥 지키기 > 
"""
import sys
import math
input = sys.stdin.readline

n, r = map(int, input().split())
min_x = min_y = int(1e9)
max_x = max_y = 0
rice = []
for _ in range(n):
    a, b = map(int, input().split())
    min_x, min_y = min(min_x, a), min(min_y, b)
    max_x, max_y = max(max_x, a), max(max_y, b)
    rice.append((a, b))

answer = 0
answer_x = answer_y = 0
for i in range(min_x, max_x + 1):
    for j in range(min_y, max_y + 1):
        count = 0
        for a, b in rice:
            if math.sqrt((i - a)**2 + (j - b)**2) <= r:
                count += 1
        if answer < count:
            answer = count
            answer_x = i
            answer_y = j

print(answer_x, answer_y)
        