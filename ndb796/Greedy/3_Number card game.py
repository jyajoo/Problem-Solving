'''
< 숫자 카드 게임 >

- 각 행마다 가장 작은 값을 구한다.
- 구해진 값들 중 가장 큰 값을 구한다.
'''

n, m = map(int, input().split())

result = 0

for i in range(n):
    arr = list(map(int, input().split()))
    a = min(arr)
    if a > result:
        result = a    # result = max(result, a)
print(result)