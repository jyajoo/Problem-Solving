"""
백준 - https://www.acmicpc.net/problem/15686

< 치킨 배달 >
"""
import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

home = []
chicken = []
for x in range(n):
    for y in range(n):
        # 집
        if city[x][y] == 1:
            home.append((x + 1, y + 1))

        elif city[x][y] == 2:
            chicken.append((x + 1, y + 1))

m_chicken = list(combinations(chicken, m))

result = 1e9
for c in m_chicken:
    temp = 0
    for x, y in home:
        dist = 1e9
        for a, b in c:
            dist = min(dist, abs(x - a) + abs(y - b))
        temp += dist
    result = min(result, temp)

print(result)
