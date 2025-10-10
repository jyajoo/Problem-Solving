'''
백준 - https://www.acmicpc.net/problem/2108

< 통계학 >

1 <= n <= 500000 (n은 홀수)
정수의 절대값은 4000을 넘지 않음
시간 복잡도 <= O(N)
'''
import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

# 1. 산술평균
print(round(sum(arr) / n))

# 2. 중앙값
arr.sort()
print(arr[n//2])

# 3. 최빈값
counter = list(Counter(arr).items())
counter.sort(key=lambda x : (-x[1], -x[0]))
numbers = []
x = counter[0][1]
for (i, j) in counter:
    if j == x:
        numbers.append(i)
    else:
        break
if len(numbers) == 1:
    print(numbers[0])
else:
    print(numbers[len(numbers) - 2])

# 4. 범위
print(arr[-1] - arr[0])