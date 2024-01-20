"""
백준 - https://www.acmicpc.net/problem/2056

< 작업 >
"""
import sys

input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
work_times = [0] * (n + 1)
times = [[0] * 2 for _ in range(n + 1)]
for i in range(1, n + 1):
    lst = list(map(int, input().split()))
    work_times[i] = lst[0]  # 시간
    indegree[i] = lst[1]  # 진입 차수

    # 선행 작업 연결하기
    for j in lst[2:]:
        graph[j].append(i)

q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    work = q.popleft()
    start, _ = times[work]
    times[work] = [start, start + work_times[work]]
    for next_work in graph[work]:
        indegree[next_work] -= 1
        if indegree[next_work] == 0:
            q.append(next_work)
        
        times[next_work][0] = max(times[next_work][0], times[work][0] + work_times[work])

times.sort(key=lambda x : -x[1])
print(times[0][1])