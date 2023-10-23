"""
백준 - https://www.acmicpc.net/problem/14888

< 연산자 끼워 넣기 >
"""
import sys

input = sys.stdin.readline


def dfs(result, i, add, sub, mul, div):
    global max_result, min_result

    if i == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return

    if add:
        dfs(result + numbers[i], i + 1, add - 1, sub, mul, div)
    if sub:
        dfs(result - numbers[i], i + 1, add, sub - 1, mul, div)
    if mul:
        dfs(result * numbers[i], i + 1, add, sub, mul - 1, div)
    if div:
        dfs(int(result / numbers[i]), i + 1, add, sub, mul, div - 1)


n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_result = -int(1e9)
min_result = int(1e9)

dfs(numbers[0], 1, add, sub, mul, div)

print(max_result)
print(min_result)

"""
- 순열 이용
- 시간 초과
- pypy3에서만 통과
"""
import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
# 덧셈, 뺄셈, 곱셈, 나눗셈
operation_cnt = list(map(int, input().split()))
operation = (
    ["+"] * operation_cnt[0]
    + ["-"] * operation_cnt[1]
    + ["*"] * operation_cnt[2]
    + ["//"] * operation_cnt[3]
)
max_result = -int(1e9)
min_result = int(1e9)
for op in permutations(operation, n - 1):
    result = numbers[0]
    for i in range(n - 1):
        if op[i] == "+":
            result += numbers[i + 1]
        elif op[i] == "-":
            result -= numbers[i + 1]
        elif op[i] == "*":
            result *= numbers[i + 1]
        else:
            result = int(result / numbers[i + 1])
    max_result = max(max_result, result)
    min_result = min(min_result, result)

print(max_result)
print(min_result)
