"""
백준 - https://www.acmicpc.net/problem/11659

< 구간 합 구하기 4 >
"""
import sys
input = sys.stdin.readline

# 수의 개수(n), 구해야 하는 횟수(m)
n, m = map(int, input().split())

numbers = list(map(int, input().split()))
result = [0] * n

result[0] = numbers[0]
for i in range(1, n):
    result[i] += result[i - 1] + numbers[i]

for _ in range(m):
    start, end = map(int, input().split())

    if start == 1:
        print(result[end - 1])
    else:
        print(result[end - 1] - result[start - 2])
