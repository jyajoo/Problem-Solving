"""
백준 - https://www.acmicpc.net/problem/13549

< 숨바꼭질 3 >
"""

from sys import stdin

input = stdin.readline

n, k = map(int, input().split())

time = [int(1e9)] * (200001)
time[n] = 0
time[n * 2] = 0
for i in range(n - 1, -1, -1):
    time[i] = time[i + 1] + 1
    time[i * 2] = min(time[i * 2], time[i])

for i in range(n + 1, k + 1):
    # x - 1, x + 1 비교
    time[i] = min(time[i], time[i - 1] + 1, time[i + 1] + 1)
    # x보다 작고 2로 나눠떨어지는 경우 비교
    if i % 2 == 0:
        time[i] = min(time[i], time[i // 2])
    # x * 2의 경우 비교
    time[i] = min(time[i], time[i * 2])
    time[i * 2] = min(time[i * 2], time[i])

print(time[k])
'''
'''
from sys import stdin

input = stdin.readline

n, k = map(int, input().split())

# dp[i] = n에서 i까지의 최소 이동 시간
dp = [int(1e9)] * (200001)
for i in range(k + 1):
    # i가 n보다 작은 경우엔 항상 x-1로만 이동이 가능하므로 n - i
    if i < n:
        dp[i] = n - i
    
    # i가 n과 같을 경우엔, 시작점이므로 0
    elif i == n:
        dp[i] = 0

    # i가 n보다 큰 경우엔, x - 1, x + 1에서 하나 건너오거나,
    # x // 2 위치에서 순간 이동하는 경우가 있다.
    else:
        dp[i] = min(dp[i], dp[i - 1], dp[i + 1]) + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2])

    # 현 위치에서 2배 뛴 곳으로 순간이동이 가능함으로 반영
    dp[2 * i] = min(dp[2 * i], dp[i])
print(dp[k])
