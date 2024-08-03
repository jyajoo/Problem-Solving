"""
백준 - https://www.acmicpc.net/problem/18353

< 병사 배치하기 >

- 첫 숫자를 선택하거나 안하거나로 나누기
"""
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.reverse()

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))