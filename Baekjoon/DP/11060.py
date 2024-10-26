"""
백준 - https://www.acmicpc.net/problem/11060

< 점프 점프 >
"""

"""
시간 초과
"""
import sys

input = sys.stdin.readline


def dfs(idx, count):
    global answer
    if idx >= len(arr):
        return
    if idx == len(arr) - 1:
        answer = min(answer, count)
        return

    a = arr[idx]
    for next in range(1, a + 1):
        dfs(idx + next, count + 1)


n = int(input())
arr = list(map(int, input().split()))
answer = int(1e9)
dfs(0, 0)
if answer == int(1e9):
    answer = -1
print(answer)

"""
"""
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [int(1e9)] * len(arr)
dp[0] = 0

for i in range(len(arr)):
    a = arr[i]
    for next in range(1, a + 1):
        if i + next < len(arr):
            dp[i + next] = min(dp[i + next], dp[i] + 1)

if dp[-1] == int(1e9):
    print(-1)
else:
    print(dp[-1])
