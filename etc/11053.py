'''
백준 - https://www.acmicpc.net/problem/11053

< 가장 긴 증가하는 부분 수열 >
'''
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [[0] * 2 for _ in range(n)]
dp[0] = [arr[0], 1]
answer = 1
for i in range(1, n):
    count = 0
    for j in range(i):
        if arr[i] > dp[j][0]:
            count = max(count, dp[j][1])
    dp[i] = [arr[i], count + 1]
    answer = max(answer, dp[i][1])

print(answer)

'''
이진탐색으로 새로운 수를 추가할 것인지,
아니면 기존의 수를 더 작은 수로 교체할 것인지 판가름이 가능ㅇ
'''
import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]

for i in range(1, n):
    idx = bisect_left(dp, arr[i])
    if idx == len(dp):
        dp.append(arr[i])
    else:
        dp[idx] = arr[i]

print(len(dp))