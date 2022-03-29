'''
< 파일 정리 >

- 확장자별로 정리하여 개수 확인
- 사전 순 정렬
'''
from collections import Counter

n = int(input())
ex = []                     # 확장자 담는 곳
for _ in range(n):
    ex.append(input().split('.')[1])
ex = dict(Counter(ex))      # Counter를 이용하여 개수 구하기 

# a = list(ex.keys())         
# a.sort()                  
a = sorted(ex.keys())       # 확장자명을 사전순으로 정렬


for i in a:
    # print(i, end = " ")
    # print(ex[i])
    print(i, ex[i])

'''
'''
n = int(input())
ex = dict()
for _ in range(n):
    a = input().split('.')[1]
    if a not in ex.keys():
        ex[a] = 1
    else:
        ex[a] += 1

