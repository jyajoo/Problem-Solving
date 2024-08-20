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
