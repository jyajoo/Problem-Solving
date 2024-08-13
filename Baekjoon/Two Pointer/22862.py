"""
백준 - https://www.acmicpc.net/problem/22862

< 가장 긴 짝수 연속한 부분 수열 (large) >
"""

from sys import stdin

input = stdin.readline

# 길이가 N인 수열 S (1 이상인 정수로 이루어짐)
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# s에서 최대 k번 원소를 삭제한 수열에서
# 짝수로 이루어져 있는 연속한 부분 수열 중 가장 긴 것 찾기
# O(N)보다 작아야 할 것

start, end = 0, 0
odd = 0
count = 0
if arr[start] % 2 == 0:
    count += 1
else:
    odd += 1
result = count
while True:
    # 홀수가 k개 이하인 경우, end 증가
    if odd <= k:
        end += 1
        if end == n:
            break

        if arr[end] % 2 == 0:
            count += 1
            result = max(result, count)
        else:
            odd += 1

    # 홀수가 k개 이상인 경우, start 증가
    else:
        if arr[start] % 2 == 0:
            count -= 1
        else:
            odd -= 1
        start += 1

print(result)
