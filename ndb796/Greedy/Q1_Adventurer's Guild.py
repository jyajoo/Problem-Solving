'''
< 모험가 길드 >

- 공포도가 x이면 반드시 x명 이상인 그룹에 속한다.
- 공포도가 낮은 순으로 그룹을 묶어 나아간다.
- Counter의 시간복잡도는 O(N)이다.
'''
from collections import Counter

n = int(input())
scared = list(map(int, input().split()))
result = 0

counter = dict(Counter(scared))     # collections의 Counter를 이용하여 공포도가 같은 사람끼리 그룹화

for key in counter.keys():
    result += counter[key] // key   # 공포도가 같은 사람 수와 공포도의 몫을 구하여 더한다.

print(result)


'''
- 공포도를 기준으로 오름차순 정렬
- 확인하는 공포도보다 모험가 수가 많으면 그룹화
'''
n = int(input())
scared = list(map(int, input().split()))
result = cnt = 0

scared.sort()

for i in scared:
    cnt += 1
    if cnt >= i:  # 공포도보다 모험가의 수가 크거나 같아지면
        result += 1
        cnt = 0

print(result)      