'''
< 회전 초밥 >
'''
import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr2 = []
result = 0
for i in range(n):
    rice = arr[i : i + k]
    if i + k > n:
        rice = arr[i:] + arr[:k - (n - i)]
    rice += [c]
    result = max(result, len(set(rice)))

print(result)

'''
'''
from collections import defaultdict
import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]

sushi_count = defaultdict(int)
# 0번째부터 k번째까지 선택 (윈도우 초기화)
for i in range(k):
    sushi_count[arr[i]] += 1

# 쿠폰 초밥 포함
sushi_count[c] += 1

max_sushi = len(sushi_count)

# 슬라이딩 윈도우
for i in range(1, n):
    new_sushi = arr[(i + k - 1) % n]
    sushi_count[new_sushi] += 1

    old_sushi = arr[i - 1]
    sushi_count[old_sushi] -= 1

    if sushi_count[old_sushi] == 0:
        del sushi_count[old_sushi]

    max_sushi = max(max_sushi, len(sushi_count))

print(max_sushi)

