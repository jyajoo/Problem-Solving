"""
백준 - https://www.acmicpc.net/problem/1932

< 정수 삼각형 >
- 시간 초과
"""
# import sys

# input = sys.stdin.readline


# def dfs(step, val, idx):
#     global answer
#     if step == n:
#         answer = max(answer, val)
#         return
#     dfs(step + 1, val + arr[step][idx], idx)
#     dfs(step + 1, val + arr[step][idx], idx + 1)


# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# answer = 0
# dfs(0, 0, 0)
# print(answer)
'''
- dp
'''
import sys

input = sys.stdin.readline

n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i - 1][j - 1]
        
        if j == i:
            up = 0
        else:
            up = dp[i - 1][j]
        
        dp[i][j] += max(up_left, up)

print(max(dp[-1]))