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

'''
'''
n, m = map(int, input().split())           # n : 볼링공의 개수, m : 볼링공의 최대 무게
balls = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
arr = [0] * 11

for i in balls:
    arr[i] += 1

result = 0
for i in range(1, m + 1):
    n -= arr[i]             # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += arr[i] * n    # A가 선택한 공의 개수 * B가 선택할 수 있는 공의 개수

print(result)
