"""
백준 - https://www.acmicpc.net/problem/15954

< 인형들 >
"""

from sys import stdin
from math import sqrt

input = stdin.readline
n, k = map(int, input().split())
dolls = list(map(int, input().split()))
result = float("inf")

# i는 인형의 시작 지점
for i in range(n - k + 1):
    # j는 k개 이상만큼
    for j in range(i + k, n + 1):
        doll_list = dolls[i:j]
        length = len(doll_list)
        m = sum(doll_list) / length
        a = 0
        for d in doll_list:
            a += (d - m) ** 2
        result = min(result, a / length)

print(sqrt(result))
"""
"""
from sys import stdin
from math import sqrt
from decimal import Decimal

input = stdin.readline
n, k = map(int, input().split())
dolls = list(map(int, input().split()))

s = [0 for _ in range(n + 1)]
e = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    s[i] = s[i - 1] + dolls[i - 1]
    e[i] = e[i - 1] + dolls[i - 1] ** 2


def calculate(start, end):
    length = end - start
    squared_avg = Decimal(e[end] - e[start]) / Decimal(length)  # 제곱 평균
    sum_avg = Decimal(s[end] - s[start]) / Decimal(length)  # 평균
    return Decimal(squared_avg - sum_avg**2)  # 분산 공식


result = float("inf")
# i는 인형의 시작 지점
for start in range(n - k + 1):
    # j는 k개 이상만큼
    for end in range(start + k, n + 1):
        v = calculate(start, end)
        result = min(result, v)

print(sqrt(result))
"""
"""
from sys import stdin
from math import sqrt

input = stdin.readline
n, k = map(int, input().split())
dolls = list(map(int, input().split()))

s = [0 for _ in range(n + 1)]
e = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    s[i] = s[i - 1] + dolls[i - 1]
    e[i] = e[i - 1] + dolls[i - 1] ** 2


def calculate(start, end):
    length = end - start
    squared_val = e[end] - e[start]
    sum_val = s[end] - s[start]
    return (length * squared_val - sum_val**2) / length**2


result = float("inf")
# i는 인형의 시작 지점
for start in range(n - k + 1):
    # j는 k개 이상만큼
    for end in range(start + k, n + 1):
        v = calculate(start, end)
        result = min(result, v)

print(sqrt(result))
