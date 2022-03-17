'''
< 모험가 길드 >

- 공포도가 x이면 반드시 x명 이상인 그룹에 속한다.
- 공포도가 낮은 순으로 그룹을 묶어 나아간다.
'''
from collections import Counter

n = int(input())
scared = list(map(int, input().split()))
result = 0

counter = dict(Counter(scared))     # collections의 Counter를 이용하여 공포도가 같은 사람끼리 그룹화

for key in counter.keys():
    result += counter[key] // key   # 공포도가 같은 사람 수와 공포도의 몫을 구하여 더한다.

print(result)