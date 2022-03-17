'''
< 볼링공 고르기 >

- 조합을 이용한다.
- 볼링공의 무게가 같은 것만 제거한다.
'''
from itertools import combinations 

n, m = map(int, input().split())  # n : 볼링공의 개수, m : 볼링공의 최대 무게
balls = list(map(int, input().split()))

combi = list(combinations(balls, 2))

for i in combi:
    if i[0] == i[1]:
        combi.remove(i)

print(len(combi))