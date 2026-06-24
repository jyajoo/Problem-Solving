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