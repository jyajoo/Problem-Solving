'''
백준 - https://www.acmicpc.net/problem/15686

< 치킨 배달 >

'''
from itertools import combinations

# 도시의 치킨 거리
def find_dist(home, chicken):
    city_dist = 0
    for i in home:
        min_val = float('inf')  # 임의의 가장 큰 수
        for j in chicken:
            dist = abs(i[0] - j[0]) + abs(i[1] - j[1])
            if min_val > dist:
                min_val = dist
        city_dist += min_val
    return city_dist

n, m = map(int, input().split())
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

home = []
chicken = []

# 집과 치킨집 구하기
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append((i + 1, j + 1))
        elif city[i][j] == 2:
            chicken.append((i + 1, j + 1))

# 최대 m개 만큼 치킨집 조합
result = list(combinations(chicken, m))

min_dist = float('inf')
for i in result:
    dist = find_dist(home, i)
    if min_dist > dist:
        min_dist = dist

# 가장 작은 도시의 치킨 거리 출력
print(min_dist)