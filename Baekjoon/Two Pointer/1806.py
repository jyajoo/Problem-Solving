"""
백준 - https://www.acmicpc.net/problem/1806

< 부분합 >
"""
import sys

input = sys.stdin.readline

# 수열의 길이, 부분합의 합 최소 기준
n, s = map(int, input().split())

arr = list(map(int, input().split()))
answer = int(1e9)

count = 0
sum_val = 0

for i in range(len(arr)):
    # 합이 s보다 작으면 더하기
    if sum_val < s:
        count += 1
        sum_val += arr[i]

    while sum_val >= s:
        answer = min(answer, count)
        sum_val -= arr[i - count + 1]
        count -= 1

if answer == int(1e9):
    print(0)
else:
    print(answer)
