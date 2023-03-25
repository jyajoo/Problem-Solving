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


'''
2023.03.25
'''
n, m = map(int, input().split())
numbers = []
for _ in range(n):
    arr = list(map(int, input().split()))
    arr.sort()
    numbers.append(arr)

result = numbers[0][0]
for i in range(n):
    if result < numbers[i][0]:
        result = numbers[i][0]
print(result)